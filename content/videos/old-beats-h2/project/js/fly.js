/* Escena 5: las portadas de la linea del tiempo SON las paginas de la rueda. Cada una vuela desde su sitio en la regla hasta la
   pose exacta de su pagina 3D (homografia sobre las 4 esquinas proyectadas por el rig) y ahi la releva la pagina real.
   Capas: la lider va al frente y cada portada que llega despues queda DETRAS de las anteriores; por eso esta capa esta debajo
   del canvas de la rueda (las que ya son pagina tapan a las que aun vuelan) y el z-index baja con el orden de llegada. */
const FLY=(function(){
  const S=200, layer=$("fly"), els=[]; let P0=[0,0], V0=[0,0], LP=[], LL=[], LD=.5, LV=1;
  function H(q){ // matriz que lleva el cuadrado (0,0)-(S,S) a 4 puntos [tl,tr,br,bl]
    const [[x0,y0],[x1,y1],[x2,y2],[x3,y3]]=q, dx1=x1-x2, dx2=x3-x2, dx3=x0-x1+x2-x3, dy1=y1-y2, dy2=y3-y2, dy3=y0-y1+y2-y3, den=dx1*dy2-dx2*dy1;
    const g=(dx3*dy2-dx2*dy3)/den, h=(dx1*dy3-dx3*dy1)/den, a=x1-x0+g*x1, b=x3-x0+h*x3, c=x0, d=y1-y0+g*y1, e=y3-y0+h*y3, f=y0;
    return `matrix3d(${a/S},${d/S},0,${g/S},${b/S},${e/S},0,${h/S},0,0,1,0,${c},${f},0,1)`; }
  function init(lab){ TL.wheelItems.forEach((f,j)=>{ const el=document.createElement("img"); el.src=`assets/gcovers/cover-${f.cov}.jpg`; el.className="flyer"; el.style.zIndex=100-j; layer.appendChild(el); els[j]={el,f,k:lab.order[j]}; });
    // la lider llega a su hueco (quieto hasta entonces) con la velocidad con la que ese hueco arranca: ella pone el aro en marcha
    const k0=lab.order[0], c=(w)=>{ const q=lab.sample(w).cards[k0].corners; return [q.reduce((a,v)=>a+(v[0]+1)*540,0)/4,q.reduce((a,v)=>a+(1-v[1])*960,0)/4]; }, a=c(T.WHEEL0), b=c(T.WHEEL0+.03);
    P0=a; V0=[(b[0]-a[0])/.03,(b[1]-a[1])/.03];
    // via de la lider: arco que sale de su sitio en la regla y entra al hueco por detras, ya en la direccion del giro. Se recorre
    // por longitud de arco con velocidad siempre creciente (0.35 v -> v, v = la del hueco al arrancar): nunca se para ni retrocede.
    const v1=Math.hypot(V0[0],V0[1]), dir=[V0[0]/v1,V0[1]/v1], f0=els[0].f; let ts=T.WH-.5, ps, Lb=0;
    for(let it=0;it<4;it++){ const q=TL.toScreen(f0.x,f0.y,ts); ps=[q.x,q.y]; const L=clamp(.9*Math.hypot(P0[0]-ps[0],P0[1]-ps[1]),110,240), C=[P0[0]-dir[0]*L,P0[1]-dir[1]*L];
      LP=[]; LL=[0]; for(let i=0;i<=60;i++){ const u=i/60; LP.push([(1-u)**2*ps[0]+2*(1-u)*u*C[0]+u*u*P0[0],(1-u)**2*ps[1]+2*(1-u)*u*C[1]+u*u*P0[1]]); if(i)LL.push(LL[i-1]+Math.hypot(LP[i][0]-LP[i-1][0],LP[i][1]-LP[i-1][1])); }
      Lb=LL[60]; LD=2*Lb/(1.35*v1); ts=T.WH-LD; }
    LV=v1; TL.setLeadStart(ts); }
  function frame(t,lab){
    if(t<T.WH-.6||t>T.WH+1.4){ layer.style.visibility="hidden"; return; } layer.style.visibility="visible";
    const smp=lab.sample(Math.max(0,T.WHEEL0+(t-T.WH))), later=[];
    els.forEach(({el,f,k},j)=>{ const a=TL.flyStart(j), b=TL.flyEnd(j); if(t<a||t>=b){ el.style.opacity=0; return; }
      const u=E.ioC(seg(t,a,b)), p=TL.toScreen(f.x,f.y,t), hs=f.size*p.z/2, c=smp.cards[k];
      // esquinas de la pagina en pantalla (tl,tr,br,bl de la imagen; por detras la textura va espejada). Si la pagina esta de canto,
      // pegada a la lente o fuera de cuadro la homografia degenera: se apunta a su pose de un instante despues, y si tampoco sirve, no se dibuja.
      const quad=(cd)=>{ const P=cd.corners.map(([x,y])=>[(x+1)*540,(1-y)*960]), d=cd.facing<0?[P[2],P[3],P[0],P[1]]:[P[3],P[2],P[1],P[0]];
        const cr=(i)=>{ const A=d[i],B=d[(i+1)%4],C=d[(i+2)%4]; return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0]); }, xs=d.map(v=>v[0]), ys=d.map(v=>v[1]);
        const good=cd.corners.every(([x,y,z])=>z<1&&Math.abs(x)<2&&Math.abs(y)<2)&&[0,1,2,3].every(i=>cr(i)>60)&&Math.max(...xs)-Math.min(...xs)<620&&Math.max(...ys)-Math.min(...ys)<620;
        return good?d:null; };
      let dst=quad(c); for(let n=1;!dst&&n<=4;n++){ later[n]=later[n]||lab.sample(Math.max(0,T.WHEEL0+(t-T.WH))+n*.05); dst=quad(later[n].cards[k]); }
      if(!dst){ el.style.opacity=0; return; }
      // vuelo: el cuadrado viaja como cuerpo rigido (centro, tamano y giro hacia los de la pagina) y solo al final se deforma
      // hasta las 4 esquinas exactas. Interpolar esquina a esquina desde lejos cruza el cuadrilatero y la homografia revienta.
      const cen=(Q)=>[(Q[0][0]+Q[1][0]+Q[2][0]+Q[3][0])/4,(Q[0][1]+Q[1][1]+Q[2][1]+Q[3][1])/4], dc=cen(dst), sc=[p.x,p.y];
      const dsz=(Math.hypot(dst[1][0]-dst[0][0],dst[1][1]-dst[0][1])+Math.hypot(dst[3][0]-dst[0][0],dst[3][1]-dst[0][1]))/2;
      let da=Math.atan2(dst[1][1]-dst[0][1],dst[1][0]-dst[0][0]); if(da>Math.PI)da-=2*Math.PI;
      let cx=lerp(sc[0],dc[0],u), cy=lerp(sc[1],dc[1],u)-150*Math.sin(Math.PI*u);
      let uu=u;
      if(j===0){ const tau=clamp(t-a,0,LD), d=.35*LV*tau+.65*LV*tau*tau/(2*LD), Lb=LL[60]; let i=1; while(i<60&&LL[i]<d)i++; const fr=clamp((d-LL[i-1])/Math.max(1e-6,LL[i]-LL[i-1]),0,1);
        cx=lerp(LP[i-1][0],LP[i][0],fr); cy=lerp(LP[i-1][1],LP[i][1],fr); uu=E.ioS(clamp(d/Lb,0,1)); }
      const h2=lerp(hs,dsz/2,uu), an=da*uu, ca=Math.cos(an), sa=Math.sin(an);
      const rigid=[[-1,-1],[1,-1],[1,1],[-1,1]].map(([x,y])=>[cx+(x*ca-y*sa)*h2,cy+(x*sa+y*ca)*h2]), wgt=E.ioC(seg(uu,.55,1));
      const q=rigid.map((r,i)=>[lerp(r[0],dst[i][0]-dc[0]+cx,wgt),lerp(r[1],dst[i][1]-dc[1]+cy,wgt)]);
      const crq=(i)=>{ const A=q[i],B=q[(i+1)%4],C=q[(i+2)%4]; return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0]); };
      if(![0,1,2,3].every(i=>crq(i)>20)){ el.style.opacity=0; return; }
      el.style.opacity=1; el.style.transform=H(q); });
  }
  return {init,frame};
})();
