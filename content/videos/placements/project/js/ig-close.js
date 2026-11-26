/* Escena 4: vuelve el mismo chat, se pega el link del pack, se envia y el artista responde. */
IG.s4=function(t){
  const el=IG.el, K=IG.kw, T=S, tap=$("tap");
  const m=E.ioC(seg(t,T.DOTS2-.02,T.DOTS2+.42)), SH=lerp(-280,-498,m);
  IG.common(t);
  // estado heredado de la escena 1
  el.story.style.transform=`translate(686px,250px) scale(${(150/860).toFixed(5)})`; el.story.style.borderRadius=(24/(150/860)).toFixed(1)+"px"; el.story.style.height=(256/(150/860)).toFixed(1)+"px"; el.stui.style.opacity=0;
  el.head.style.transform="none"; el.inp.style.transform="none"; el.ts.style.opacity=el.cap.style.opacity=1; el.thread.style.transform=`translateY(${SH.toFixed(1)}px)`; el.story.style.marginTop=SH.toFixed(1)+"px";
  el.bme.style.opacity=1; el.bme.style.transform="none"; el.bme.style.background=""; el.dots.style.opacity=0; el.athem.style.opacity=1; el.bthem.style.opacity=1; el.bthem.style.transform="none";
  // camara: A = cerca del hilo y el campo de texto; B = el telefono baja y deja la mitad superior a la tipografia
  const inn=1-E.outC(seg(t,T.BACK-.02,T.BACK+.32));
  let s=lerp(1.1,.92,m)*(1+pulse(t,T.SENDL,.016,12,24)+pulse(t,W.READY2,.02,11,24)+pulse(t,T.FIRE,.035,9,22))+.05*E.outC(seg(t,T.ACC,T.ACC+.3))+(t-T.BACK)*.004;
  const c={fx:540,fy:130,s,sx:540+inn*1700,sy:lerp(-57,664,m),ry:inn*18+lerp(0,-7,m),rx:lerp(0,3,m),rz:lerp(0,1.2,m),blur:inn*10};
  // mini zoom final hacia el FIRE: el globo queda como punto fijo y crece
  { const zf=.08*E.ioC(seg(t,T.FIRE+.15,T.ACC))+.06*E.outC(seg(t,T.ACC,T.ACC+.25)), py=130+IG.FIRETOP+SH+48, Px=c.sx+(280-c.fx)*c.s, Py=c.sy+(py-c.fy)*c.s;
    c.s*=1+zf; c.sx=Px-zf*420-(280-c.fx)*c.s; c.sy=Py+zf*120-(py-c.fy)*c.s; }
  IG.setCam(c);
  // el link llega volando desde la Gallery y cae en el campo de texto
  const chip=DESK.chip, q=E.ioC(seg(t,T.BACK,T.PASTE)), tgt=IG.toScreen(c,108+190,1388), w=chip.offsetWidth;
  chip.style.opacity=(t<T.PASTE?1-seg(q,.82,1):0).toFixed(3);
  chip.style.transform=`translate(${(lerp(540,tgt.x,q)-w/2).toFixed(1)}px,${(lerp(600,tgt.y,q)-48-Math.sin(Math.PI*q)*120).toFixed(1)}px) scale(${lerp(1.22,.92,q).toFixed(4)}) rotate(${(-4*(1-q)).toFixed(2)}deg)`;
  const pasted=t>=T.PASTE-.04&&t<T.SENDL;
  el.inTxt.style.opacity=pasted?E.outC(seg(t,T.PASTE-.04,T.PASTE+.06)).toFixed(3):0; el.inTxt.style.transform=`scale(${(1+pulse(t,T.PASTE,.06,13,26)).toFixed(4)})`; el.inTxt.style.transformOrigin="0 50%";
  el.inPh.style.opacity=pasted?0:1; el.inSend.style.opacity=pasted?1:0; el.inMic.style.opacity=el.inImg.style.opacity=pasted?0:1;
  el.inSend.style.transform=`scale(${(1-pulse(t,T.SENDL-.02,.12,12,24)).toFixed(4)})`;
  // enviar: la tarjeta del pack sube al hilo
  const la=seg(t,T.SENDL,T.SENDL+.28); el.link.style.opacity=t>=T.SENDL?1:0;
  el.link.style.transform=`translateY(${((1-E.outC(la))*520).toFixed(1)}px) scale(${(la<=0?.6:.6+.4*E.outB(la)).toFixed(4)})`;
  el.seen.style.opacity=(seg(t,T.SENDL+.42,T.SENDL+.52)*(1-seg(t,T.FIRE-.05,T.FIRE))).toFixed(3);
  // el artista escribe y responde
  const da=seg(t,T.DOTS2,T.DOTS2+.12)*(1-seg(t,T.FIRE-.03,T.FIRE));
  el.dots2.style.opacity=da>0?1:0; el.dots2.style.transform=`scale(${(da<=0?.4:.4+.6*E.outB(Math.min(1,da))).toFixed(3)})`;
  el.dot2I.forEach((d,k)=>{d.style.transform=`translateY(${(-7*Math.max(0,Math.sin((t-T.DOTS2)*16-k*.9))).toFixed(1)}px)`;});
  el.athem2.style.opacity=seg(t,T.DOTS2,T.DOTS2+.1).toFixed(3);
  const fa=seg(t,T.FIRE,T.FIRE+.22); el.bfire.style.opacity=t>=T.FIRE?1:0; el.bfire.style.transform=`scale(${(fa<=0?.4:(.4+.6*E.outB(fa))*(1+pulse(t,T.ACC,.06,10,22))).toFixed(4)})`;
  // toque en Send
  const tp=IG.toScreen(c,770,1388), tu=seg(t,T.SENDL,T.SENDL+.3);
  if(t>=T.SENDL-.1&&tu<1){ tap.style.background="rgba(255,255,255,.55)"; tap.style.border="none"; tap.style.opacity=(t<T.SENDL?.5*seg(t,T.SENDL-.1,T.SENDL):.5*(1-tu)).toFixed(3);
    tap.style.transform=`translate(${tp.x.toFixed(1)}px,${tp.y.toFixed(1)}px) scale(${(t<T.SENDL?.5:.5+1.3*E.outC(tu)).toFixed(3)})`; } else tap.style.opacity=0;
  // tipografia
  [...K.ASAP,...K.FIRST].forEach(w=>w.put(0,0,{o:0}));
  { const sl=slam(t,W.OPP,.13), out=E.inC(seg(t,T.SENDL-.14,T.SENDL+.04)); K.OPP.put(540,860-out*900-(t-W.OPP)*20,{o:sl.o*(out<1?1:0),s:sl.s,by:out>0?40:sl.b}); }
  { const sl=slam(t,W.IM,.12); K.IM.put(120+K.IM.w/2,300,{o:sl.o,s:sl.s,by:sl.b}); }
  { const sl=slam(t,W.READY2,.13); K.READY.put(540,300+K.IM.h*.5+K.READY.h*.56,{o:sl.o,s:sl.s*(1+pulse(t,T.ACC,.03,10,22)),by:sl.b}); }
};
