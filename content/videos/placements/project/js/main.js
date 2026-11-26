/* Una sola funcion pura frame(t): cada escena calcula todos sus estilos desde cero. */
const grain=$("grain"), bgglow=$("bgglow");
function frame(t){
  ktCheck();
  const fr=Math.round(t*30); grain.style.backgroundPosition=`${(fr*37)%256}px ${(fr*91)%256}px`;
  const igA=t<HOOK.DUR?1-seg(t,HOOK.WHIP,HOOK.DUR):seg(t,S.BACK-.1,S.BACK+.2)*(1+.5*seg(t,C.T,C.T+.3));
  bgglow.style.background=`radial-gradient(ellipse 80% 55% at ${(50+Math.sin(t*.6)*8).toFixed(1)}% ${(40+Math.cos(t*.5)*6).toFixed(1)}%, rgba(${Math.round(lerp(30,96,igA))},${Math.round(lerp(30,38,igA))},${Math.round(lerp(34,160,igA))},${lerp(.55,.42,igA).toFixed(3)}) 0%, rgba(10,10,12,0) 70%)`;
  DESK.frame(t); IG.frame(t); CTA.frame(t);
}
const driver={}; let _t=0; Object.defineProperty(driver,"t",{get(){return _t;},set(v){_t=v;frame(v);}});
window.__timelines=window.__timelines||{};
const tl=gsap.timeline({paused:true});
tl.to(driver,{t:DUR,duration:DUR,ease:"none"},0);
window.__timelines["main"]=tl;
tl.seek(0); frame(0);
