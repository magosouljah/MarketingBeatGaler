/* Cierre: Comment "GALER" to try it for free. Una palabra por golpe de voz; GALER va en una pastilla blanca. */
const CTA=(function(){
  const W1=KW("COMMENT",720), G=KW("GALER",700), W2=KW("TO TRY IT",600), W3=KW("FOR FREE",600);
  G.el.style.cssText+=";background:#f5f5f5;color:#0c0c0c;text-shadow:none;padding:.16em .3em .2em;border-radius:.42em;box-shadow:0 30px 90px rgba(120,80,255,.45),0 12px 30px rgba(0,0,0,.5)";
  G.measure(); 
  function frame(t){
    if(t<C.T-.05){ [W1,G,W2,W3].forEach(w=>w.put(0,0,{o:0})); return; }
    const dr=(t-C.T)*8, end=1+pulse(t,C.END,.03,9,20);
    { const sl=slam(t,C.COMMENT,.13); W1.put(540,640-dr,{o:sl.o,s:sl.s*end,by:sl.b}); }
    { const g=seg(t,C.GALER,C.GALER+.18), q=g<=0?0:E.outB(g); G.put(540,640+W1.h*.5+34+G.fs*.61-dr,{o:t>=C.GALER?1:0,s:(.5+.5*q)*(1+pulse(t,22.05,.035,10,22))*end,r:lerp(-8,-2.5,q)}); }
    const y2=640+W1.h*.5+34+G.fs*1.22+44;
    { const sl=slam(t,C.TO,.12); W2.put(540,y2+W2.h*.5-dr,{o:sl.o,s:sl.s*end,by:sl.b}); }
    { const sl=slam(t,C.FOR,.12); W3.put(540,y2+W2.h*1.55-dr,{o:sl.o,s:sl.s*end,by:sl.b}); }
  }
  return {frame};
})();
