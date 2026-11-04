"""Deterministic local browser QA fallback; NOT a substitute for HyperFrames WebGL review."""
import argparse, asyncio, os, pathlib, io, subprocess, threading, base64, json
from PIL import Image
from playwright.async_api import async_playwright
ROOT=pathlib.Path(__file__).resolve().parents[1]
async def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default=str(ROOT/'orbit-local-qa.mp4'));p.add_argument('--frames',type=int,default=144);p.add_argument('--fps',type=int,default=24);p.add_argument('--width',type=int,default=720);p.add_argument('--height',type=int,default=1280);p.add_argument('--shots',action='store_true');args=p.parse_args()
 async with async_playwright() as pw:
    browser=await pw.chromium.launch(executable_path='/usr/bin/chromium' if os.path.isfile('/usr/bin/chromium') else None,headless=True,args=['--no-sandbox','--enable-webgl','--use-gl=angle','--use-angle=swiftshader'])
    page=await browser.new_page(viewport={'width':args.width,'height':args.height},device_scale_factor=1)
    page.on('pageerror',lambda e:print('PAGE ERROR',e))
    html=(ROOT/'index.html').read_text()
    data=[]
    for i in range(24):
      ext='avif' if i>=20 else 'jpg'
      raw=(ROOT/'assets'/'covers'/f'cover-{i+1:02d}.{ext}').read_bytes()
      data.append(f'data:image/{ext};base64,'+base64.b64encode(raw).decode())
    html=html.replace('<script>','<script>window.__embeddedCovers='+json.dumps(data)+';</script><script>',1)
    await page.set_content(html,wait_until='load')
    await page.wait_for_function('window.__orbit && (window.__orbit.ready || window.__orbit.error)',timeout=30000)
    s=await page.evaluate('({ready:window.__orbit?.ready,error:window.__orbit?.error,gl:!!document.querySelector("canvas").getContext("webgl2")})')
    print('render context',s,flush=True)
    if not s['ready']:raise RuntimeError(str(s['error']))
    canvas=page.locator('#stage')
    if args.shots:
      for t in [0,.75,1.7,2.8,4.2,5.7]:
        await page.evaluate('(t)=>seekTo(t)',t)
        target=ROOT/f'snapshot-{t:.2f}.png';await canvas.screenshot(path=str(target))
    if args.frames:
      proc=subprocess.Popen(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{args.width}x{args.height}','-r',str(args.fps),'-i','pipe:0','-an','-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-movflags','+faststart',args.output],stdin=subprocess.PIPE)
      for frame in range(args.frames):
        t=5.8*frame/(args.frames-1)
        await page.evaluate('(t)=>seekTo(t)',t)
        shot=await canvas.screenshot(type='png')
        proc.stdin.write(Image.open(io.BytesIO(shot)).convert('RGB').tobytes())
        if frame%24==0:print('capturing',frame,'/',args.frames,flush=True)
      proc.stdin.close();proc.wait()
      if proc.returncode!=0:raise RuntimeError('ffmpeg failed')
      print('video',args.output,'size',os.path.getsize(args.output),flush=True)
    await browser.close()
if __name__=='__main__':asyncio.run(main())
