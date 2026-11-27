/* Escenas 2-4: lienzo blanco con las dos ventanas de FL Studio (grabaciones reales, 1920x1052) y el drag & drop del clip.
   El clip arrastrado es un recorte del propio clip ZENOLOGY de Track 1; al soltarlo cae sobre Track 1 del proyecto nuevo (Pattern 2). */
const FL=(function(){
  const NOLD=CLIP.nOld, NNEW=CLIP.nNew, NX=3300, DR=V.drag, RATE=((16.73-OLD0)-(T.TS-T.OLD))/(T.TE-T.TS), SCROLL=220.4/(8*60/130*4)*RATE, CL={x:CLIP.x0,y:147,w:CLIP.x1-CLIP.x0,h:50}, G={x:115,y:27}, LANE={x:NX+V.time.LANEX,y:147};
  const fl=$("fl"), bg=$("flbg"), w=$("flw"), io=$("imgOld"), im=$("imgNew"), lane=$("lane"), dropfx=$("dropfx"), grabfx=$("grabfx"), clip=$("clip");
  clip.style.transformOrigin=`${G.x}px ${G.y}px`;
  const src=(d,i)=>`assets/fl/${d}/${String(i).padStart(4,"0")}.jpg`;
  io.src=src("viejo",1); im.src=src("nuevo",1); let curO=1, curN=1;
  const ready=Promise.all([io.decode(),im.decode()]);
  const P0={x:CL.x+G.x,y:CL.y+G.y}, P1={x:LANE.x+G.x,y:LANE.y+G.y-36};
  /* cursor en el mundo de FL */
  function cw(t){
    if(t<=T.LIFT) return {x:P0.x+(T.LIFT-Math.max(t,T.GRAB-.6))*SCROLL,y:P0.y};
    const u=seg(t,T.LIFT,T.ARRIVE), e=lerp(E.ioS(u),E.ioC(u),.55);
    const y=lerp(P0.y,P1.y,e)+DR.arc*Math.sin(Math.PI*e)+DR.wob*Math.sin(u*Math.PI*3)*(1-u);
    const drop=t>T.D?36*E.outC(seg(t,T.D,T.D+.08)):0;
    return {x:lerp(P0.x,P1.x,e),y:y+drop};
  }
  /* clip con peso: muelle subamortiguado hacia el cursor + inclinacion segun la velocidad (tabla a 240 Hz, pura en t) */
  const DT=1/240, N=Math.ceil((T.D-T.LIFT+.02)/DT)+2, SX=new Float32Array(N), SY=new Float32Array(N), SR=new Float32Array(N);
  (function(){ let px=CL.x,py=CL.y,vx=-SCROLL,vy=0,r=0; const K=DR.K,C=DR.C;
    for(let i=0;i<N;i++){ const t=T.LIFT+i*DT, c=cw(t), tx=c.x-G.x, ty=c.y-G.y;
      SX[i]=px; SY[i]=py; SR[i]=r;
      vx+=(K*(tx-px)-C*vx)*DT; vy+=(K*(ty-py)-C*vy+900*0)*DT; px+=vx*DT; py+=vy*DT;
      const rt=clamp(vx*DR.tilt,-17,17)+clamp(vy*.006,-5,5); r+=(rt-r)*Math.min(1,DT/.07); } })();
  const tab=(A,t)=>{ const x=clamp((t-T.LIFT)/DT,0,N-1.001), i=Math.floor(x); return A[i]+(A[i+1]-A[i])*(x-i); };
  /* pantalla completa: z >= 1920/1052 mientras se escucha; solo se abre el plano durante el viaje del clip */
  const kcx=t=>kf(t,[[T.OLD,1010],[T.OLDDROP,990,E.ioS],[T.LIFT+.1,1010,E.ioS],[T.ARRIVE+.1,NX+985,E.ioS],[T.NEWDROP,NX+1000,E.ioS],[T.OUT,NX+1030,E.ioS]]);
  const kcy=t=>526;
  const kz=t=>kf(t,[[T.OLD-.12,1.45],[T.OLD+.26,1.84,E.outC],[T.OLDDROP-.05,1.87,E.ioS],[T.OLDDROP+.22,1.97,E.outE],[T.LIFT+.1,1.92,E.ioS],[T.ARRIVE+.1,1.87,E.ioS],[T.NEWDROP-.05,1.9,E.ioS],[T.NEWDROP+.22,2.02,E.outE],[T.OUT,2.05,E.ioS]])
      -DR.dip*Math.sin(Math.PI*seg(t,T.LIFT+.15,T.ARRIVE+.1))+pulse(t,T.D,.05,9,20)+pulse(t,T.OLDDROP,.015,9,20)+pulse(t,T.NEWDROP,.015,9,20);
  const cam=t=>({cx:kcx(t),cy:kcy(t),z:kz(t)});
  const toScreen=(x,y,t)=>{ const c=cam(t); return {x:540+(x-c.cx)*c.z,y:960+(y-c.cy)*c.z}; };
  async function frame(t){
    const on=t>=T.OLD-.14&&t<T.OUT+.46; fl.style.visibility=on?"visible":"hidden"; if(!on)return;
    const c=cam(t); w.style.transform=`translate(540px,960px) scale(${c.z.toFixed(5)}) translate(${(-c.cx).toFixed(2)}px,${(-c.cy).toFixed(2)}px)`;
    /* entrada desde el arranque y salida: la ventana nueva se encoge hasta ser un archivo mas de la linea del tiempo */
    let op=seg(t,T.OLD-.12,T.OLD+.02), tr="none";
    if(t>=T.OUT){ const p=TL.toScreen(TL.NEWF.x,TL.NEWF.y,T.OUT+.25), u=E.ioC(seg(t,T.OUT,T.OUT+.42)); fl.style.transformOrigin=`${p.x.toFixed(1)}px ${p.y.toFixed(1)}px`; tr=`scale(${lerp(1,.035,u).toFixed(5)})`; op=1-seg(t,T.OUT+.33,T.OUT+.43); bg.style.opacity=(1-seg(t,T.OUT,T.OUT+.1)).toFixed(3); }
    else bg.style.opacity=1;
    fl.style.opacity=op.toFixed(3); fl.style.transform=tr;
    /* frames reales */
    const vo=t<=T.TS?t-T.OLD:(T.TS-T.OLD)+(t-T.TS)*RATE, a=clamp(Math.floor(vo*30+1e-4)+1,1,NOLD), b=clamp(Math.floor((t-T.D)*30+1e-4)+1,1,NNEW), jobs=[];
    if(a!==curO){ curO=a; io.src=src("viejo",a); jobs.push(io.decode()); }
    if(b!==curN){ curN=b; im.src=src("nuevo",b); jobs.push(im.decode()); }
    if(jobs.length) await Promise.all(jobs);
    /* agarre, arrastre y caida */
    const gx=CL.x+(T.LIFT-t)*SCROLL;
    grabfx.style.opacity=(t>=T.GRAB&&t<T.LIFT+.05?seg(t,T.GRAB,T.GRAB+.05):0).toFixed(3); grabfx.style.width=CL.w+"px"; grabfx.style.transform=`translate(${gx.toFixed(1)}px,${CL.y}px)`;
    if(t>=T.LIFT&&t<T.D+.3){ const u=E.outB(seg(t,T.D,T.D+.16)); const x=lerp(tab(SX,Math.min(t,T.D)),LANE.x,t<T.D?0:u), y=lerp(tab(SY,Math.min(t,T.D)),LANE.y,t<T.D?0:u), r=tab(SR,Math.min(t,T.D))*(1-seg(t,T.D,T.D+.1));
      const s=t<T.D?1+.16*E.outB(seg(t,T.LIFT,T.LIFT+.2)):lerp(1.16,1,E.outC(seg(t,T.D,T.D+.12)));
      clip.style.opacity=(1-seg(t,T.D+.12,T.D+.26)).toFixed(3); clip.style.transform=`translate(${x.toFixed(2)}px,${y.toFixed(2)}px) rotate(${r.toFixed(2)}deg) scale(${s.toFixed(4)})`; }
    else clip.style.opacity=0;
    lane.style.opacity=(1-seg(t,T.D+.03,T.D+.14)).toFixed(3);
    dropfx.style.opacity=(t>=T.D?.55*(1-seg(t,T.D,T.D+.3)):0).toFixed(3);
  }
  return {frame,ready,cam,toScreen,cw,NX};
})();
