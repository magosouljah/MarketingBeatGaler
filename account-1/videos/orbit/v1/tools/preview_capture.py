"""Fallback deterministic browser capture, for visual QA only. HyperFrames is the approved primary renderer."""
import argparse, asyncio, os, pathlib, io, subprocess, base64, json
from PIL import Image
from playwright.async_api import async_playwright

ROOT=pathlib.Path(__file__).resolve().parents[1]

async def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',default=str(ROOT/'orbit-local-qa.mp4'))
    p.add_argument('--frames',type=int,default=144)
    p.add_argument('--fps',type=int,default=24)
    p.add_argument('--width',type=int,default=720)
    p.add_argument('--height',type=int,default=1280)
    p.add_argument('--shots',action='store_true')
    a=p.parse_args()
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(
            executable_path='/usr/bin/chromium' if os.path.isfile('/usr/bin/chromium') else None,
            headless=True,
            args=['--no-sandbox','--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']
        )
        page=await browser.new_page(viewport={'width':a.width,'height':a.height},device_scale_factor=1)
        html=(ROOT/'index.html').read_text()
        covers=[]
        for i in range(24):
            ext='avif' if i>=20 else 'jpg'
            raw=(ROOT/'assets'/'covers'/f'cover-{i+1:02d}.{ext}').read_bytes()
            covers.append(f'data:image/{ext};base64,'+base64.b64encode(raw).decode())
        html=html.replace('<script>','<script>window.__embeddedCovers='+json.dumps(covers)+';</script><script>',1)
        await page.set_content(html,wait_until='load')
        await page.wait_for_function('window.__orbit && (window.__orbit.ready || window.__orbit.error)',timeout=30000)
        report=await page.evaluate('({ready:window.__orbit?.ready,error:window.__orbit?.error,webgl:!!document.querySelector("canvas").getContext("webgl2")})')
        print('Render context:',report,flush=True)
        if not report['ready']:
            raise RuntimeError(report['error'])
        # Disable the human-preview timer. All captured images are seeked at an exact timestamp.
        await page.evaluate('()=>window.dispatchEvent(new CustomEvent("hf-seek",{detail:{time:0}}))')
        stage=page.locator('#stage')
        if a.shots:
            for t in [0,.75,1.7,2.8,4.2,5.7]:
                await page.evaluate('(t)=>seekTo(t)',t)
                await stage.screenshot(path=str(ROOT/f'snapshot-{t:.2f}.png'))
        if a.frames:
            command=['ffmpeg','-y','-hide_banner','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{a.width}x{a.height}','-r',str(a.fps),'-i','pipe:0','-an','-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-movflags','+faststart',a.output]
            proc=subprocess.Popen(command,stdin=subprocess.PIPE)
            for frame in range(a.frames):
                t=5.8*frame/(a.frames-1)
                await page.evaluate('(t)=>seekTo(t)',t)
                png=await stage.screenshot(type='png')
                proc.stdin.write(Image.open(io.BytesIO(png)).convert('RGB').tobytes())
                if frame%24==0:print('capturing',frame,'/',a.frames,flush=True)
            proc.stdin.close()
            proc.wait()
            if proc.returncode!=0:raise RuntimeError('FFmpeg failed')
            print('MP4:',a.output,'bytes:',os.path.getsize(a.output),flush=True)
        await browser.close()

if __name__=='__main__':asyncio.run(main())
