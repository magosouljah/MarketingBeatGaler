/* Cursor-personaje (mano de pixeles de la app, heredado de add-finder), en espacio de pantalla.
   CURSOR.path = [[t0,t1,x,y], ...]  mueve desde la posicion anterior hasta (x,y) entre t0 y t1.
   CURSOR.clicks = [t, ...]  cada clic: llega, se queda quieto, se encoge, suelta.  CURSOR.vis = [[a,b], ...] */
const CURSOR=(function(){
  const CUR=[[8,1,2],[8,2,2],[8,3,2],[8,4,2],[8,5,2],[8,6,2],[5,7,2],[8,7,2],[11,7,2],[5,8,2],[8,8,2],[11,8,2],[14,8,1],[5,9,2],[8,9,2],[11,9,2],[14,9,2],[1,10,2],[5,10,8],[14,10,2],[1,11,3],[5,11,11],[2,12,14],[3,13,13],[3,14,13],[4,15,11],[4,16,11],[5,17,10],[5,18,9],[6,19,8],[6,20,8]];
  const el=$("cursor"), svg=el.querySelector("svg"); let s1="",s2="";
  CUR.forEach(([x,y,w])=>{s1+=`<rect x="${x-1}" y="${y-1}" width="${w+2}" height="3" fill="#0d0d0d"/>`;s2+=`<rect x="${x}" y="${y}" width="${w}" height="1.02" fill="#ffffff"/>`;});
  svg.innerHTML=s1+s2;
  const o={path:[],clicks:[],vis:[],start:[1000,2100],
    pos(t){ let x=this.start[0], y=this.start[1]; for(const [a,b,px,py] of this.path){ if(t<=a)break; const u=E.ioS(seg(t,a,b)); x=lerp(x,px,u); y=lerp(y,py,u); } return {x,y}; },
    draw(t){ const tap=$("tap"); const on=this.vis.some(([a,b])=>t>=a&&t<=b); el.style.opacity=on?1:0;
      let tOp=0,tTr=""; for(const tc of this.clicks){ const tu=seg(t,tc,tc+.3); if(t>=tc&&tu<1){ const p=this.pos(tc); tOp=.9*(1-tu); tTr=`translate(${p.x.toFixed(1)}px,${(p.y+4).toFixed(1)}px) scale(${(.25+1.3*E.outC(tu)).toFixed(3)})`; } }
      if(on||tOp>0){ tap.style.background="none"; tap.style.border="6px solid rgba(255,255,255,.92)"; tap.style.opacity=tOp.toFixed(3); if(tTr)tap.style.transform=tTr; }
      if(!on)return;
      const p=this.pos(t), a=this.pos(t-1/90), b=this.pos(t+1/90), vx=(b.x-a.x)*45, vy=(b.y-a.y)*45, sp=Math.hypot(vx,vy), ang=Math.atan2(vy,vx)*180/Math.PI, st=1+clamp(sp/5200,0,.42);
      let press=1, lift=0; for(const tc of this.clicks){ if(Math.abs(t-tc)>.5)continue;
        press*=kf(t,[[tc-.5,1],[tc-.2,1],[tc-.03,1.07,E.ioS],[tc+.045,.74,E.outC],[tc+.14,.76,E.lin],[tc+.26,1.05,E.outC],[tc+.34,1,E.ioS]]);
        lift+=kf(t,[[tc-.5,0],[tc-.2,0],[tc-.03,-9,E.ioS],[tc+.045,4,E.outC],[tc+.26,0,E.outC]]); }
      const rot=clamp(vx/260,-12,12)*.5, breathe=1+(sp<8?Math.sin(t*5.2)*.018:0);
      el.style.transform=`translate(${p.x.toFixed(2)}px,${(p.y+lift).toFixed(2)}px) rotate(${ang.toFixed(2)}deg) scale(${st.toFixed(4)},${(1/Math.sqrt(st)).toFixed(4)}) rotate(${(-ang).toFixed(2)}deg) rotate(${rot.toFixed(2)}deg) scale(${press.toFixed(4)},${(press*breathe).toFixed(4)})`;
    }};
  return o;
})();
