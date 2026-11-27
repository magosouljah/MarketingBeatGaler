/* Cursor-personaje (mano de pixeles de add-finder/placements) en espacio de pantalla. Clics en el menu y agarre sostenido durante el arrastre. */
const CUR=(function(){
  const CURP=[[8,1,2],[8,2,2],[8,3,2],[8,4,2],[8,5,2],[8,6,2],[5,7,2],[8,7,2],[11,7,2],[5,8,2],[8,8,2],[11,8,2],[14,8,1],[5,9,2],[8,9,2],[11,9,2],[14,9,2],[1,10,2],[5,10,8],[14,10,2],[1,11,3],[5,11,11],[2,12,14],[3,13,13],[3,14,13],[4,15,11],[4,16,11],[5,17,10],[5,18,9],[6,19,8],[6,20,8]];
  const el=$("cursor"), svg=el.querySelector("svg"), tap=$("tap"); let s1="",s2="";
  CURP.forEach(([x,y,w])=>{s1+=`<rect x="${x-1}" y="${y-1}" width="${w+2}" height="3" fill="#0d0d0d"/>`;s2+=`<rect x="${x}" y="${y}" width="${w}" height="1.02" fill="#ffffff"/>`;}); svg.innerHTML=s1+s2;
  const CARD=TL.CARD, ITEM={x:TL.MENU.x+170,y:TL.MENU.y+52}, CLICKS=[T.RCLICK,T.OPEN];
  const IC=V.introCursor?V.introCursor(TL.HV):null;      // cursor propio de la intro de la variante
  function pos(t){
    if(IC&&t<IC.b) return IC.pos(t,TL.toScreen);
    if(t<T.OLD){ let x=kf(t,[[T.GAL-.1,900],[T.RCLICK-.1,CARD.x,E.ioS],[T.RCLICK+.16,CARD.x],[T.OPEN-.1,ITEM.x,E.ioS]]), y=kf(t,[[T.GAL-.1,1720],[T.RCLICK-.1,CARD.y,E.ioS],[T.RCLICK+.16,CARD.y],[T.OPEN-.1,ITEM.y,E.ioS]]); return {x,y}; }
    const g=t=>{ const c=FL.cw(t); return FL.toScreen(c.x,c.y,t); };
    if(t<T.GRAB-.05){ const a=g(T.GRAB-.05), u=E.ioS(seg(t,T.GRAB-.55,T.GRAB-.05)); return {x:lerp(900,a.x,u),y:lerp(1560,a.y,u)}; }
    const p=g(t), u=E.ioS(seg(t,T.D+.1,T.D+.5)); return {x:p.x+150*u,y:p.y+330*u};
  }
  function frame(t){
    const on=(IC&&t>=IC.a&&t<IC.b)||(t>=T.GAL-.1&&t<T.SPLASH+.04)||(t>=T.GRAB-.55&&t<T.D+.5); el.style.opacity=on?(t>T.D?1-seg(t,T.D+.3,T.D+.5):1):0;
    let tOp=0,tTr=""; for(const tc of [...CLICKS,T.D]){ const tu=seg(t,tc,tc+.3); if(t>=tc&&tu<1){ const p=pos(tc); tOp=.9*(1-tu); tTr=`translate(${p.x.toFixed(1)}px,${(p.y+4).toFixed(1)}px) scale(${(.25+1.3*E.outC(tu)).toFixed(3)})`; } }
    tap.style.opacity=tOp.toFixed(3); if(tTr)tap.style.transform=tTr;
    if(!on)return;
    const p=pos(t), a=pos(t-1/90), b=pos(t+1/90), vx=(b.x-a.x)*45;
    let press=1, lift=0; for(const tc of CLICKS){ if(Math.abs(t-tc)>.5)continue;
      press*=kf(t,[[tc-.5,1],[tc-.2,1],[tc-.03,1.07,E.ioS],[tc+.045,.74,E.outC],[tc+.14,.76,E.lin],[tc+.26,1.05,E.outC],[tc+.34,1,E.ioS]]);
      lift+=kf(t,[[tc-.5,0],[tc-.2,0],[tc-.03,-9,E.ioS],[tc+.045,4,E.outC],[tc+.26,0,E.outC]]); }
    press*=kf(t,[[T.GRAB-.08,1],[T.GRAB-.02,1.08,E.ioS],[T.GRAB+.05,.78,E.outC],[T.D,.78],[T.D+.12,1.08,E.outC],[T.D+.22,1,E.ioS]]);
    el.style.transform=`translate(${p.x.toFixed(2)}px,${(p.y+lift).toFixed(2)}px) rotate(${(clamp(vx/260,-12,12)*.5).toFixed(2)}deg) scale(${press.toFixed(4)})`;
  }
  return {frame,pos};
})();
