/* Escena 1 (viaje por la linea del tiempo + Gallery + menu + arranque de FL) y la mitad 2D de la escena 5.
   Un mundo con camara: pantalla = (540,960) + (mundo - c) * z. Nada se encima: cada cosa reserva su caja antes de colocarse. */
const TL=(function(){
  const YS=3000, X=y=>(y-2026)*YS, XL=X(2022)-300, XR=X(2027)+650, XF=XL+270, TX=X(2023)+1500, TY=-330, CSZ=360, GS=CSZ/304, NEWF={x:2620,y:-400}, RED="#e3261b";
  const tl=$("tl"), w=$("tlw"), mbfe=$("mbfe"), rpath=$("rpath"), ruler=$("ruler");
  const rnd=mulberry(4117);
  /* regla: empieza en un tope (el principio de todo) y sigue hacia 2027 */
  rpath.setAttribute("d",`M${XL} 0 L${XR} 0 M${XL} -70 L${XL} 70 M${XR-70} -50 L${XR} 0 L${XR-70} 50`); rpath.setAttribute("stroke-width","9");
  let h=""; for(let x=XL+250;x<=XR-200;x+=250){ const major=Math.abs(x%YS)<1; h+=`<div class="tick" style="left:${x-3}px;top:${major?-60:-22}px;height:${major?120:44}px"></div>`; } $("ticks").innerHTML=h;
  $("years").innerHTML=[2022,2023,2024,2025,2026,2027].map(y=>`<div class="yr" style="left:${X(y)}px">${y}</div>`).join("");
  /* cajas reservadas: [x0,x1,lado] lado -1 arriba, 1 abajo */
  const zones=[]; const reserve=(x0,x1,side)=>zones.push([x0,x1,side]);
  /* notas manuscritas en rojo con flecha a la regla: [texto, x, lado, giro, x de la punta] */
  const NOTES=[["First beat",XF+500,-1,-5,XF+900],["SoundCloud",X(2022)+1600,1,4,X(2022)+900],["PluggnB era",X(2022)+2500,-1,-4,X(2022)+3250],["Rage era",TX-60,1,4,TX+480],["Favorite beat",X(2024)+1300,-1,-4,X(2024)+560],["First placement",X(2025)+1500,1,3,X(2025)+600]];
  const NW=s=>s.length*86+60, NY=620;
  const arrow=(ax,ay,bx,by)=>{ const mx=(ax+bx)/2+(by-ay)*.16, my=(ay+by)/2-(bx-ax)*.16, a=Math.atan2(by-my,bx-mx), L=64, p=(d)=>`${(bx-L*Math.cos(a+d)).toFixed(0)} ${(by-L*Math.sin(a+d)).toFixed(0)}`;
    return `<path d="M${ax.toFixed(0)} ${ay.toFixed(0)} Q${mx.toFixed(0)} ${my.toFixed(0)} ${bx} ${by} M${p(.5)} L${bx} ${by} L${p(-.42)}" fill="none" stroke="${RED}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>`; };
  let nh="", ah="";
  for(const [s,x,side,r,bx] of NOTES){ const wd=NW(s), y=side*NY, left=bx<x; nh+=`<div class="note" style="left:${x}px;top:${y}px;transform:translate(-50%,-50%) rotate(${r}deg)">${s}</div>`;
    const ax=x+(left?-wd/2-30:wd/2+30), ay=y-side*40; ah+=arrow(ax,ay,bx,side*(side>0?330:80));
    reserve(Math.min(x-wd/2,bx)-170,Math.max(x+wd/2,bx)+170,side); }
  $("notes").innerHTML=nh+`<svg class="arrows" width="10" height="10">${ah}</svg>`;
  const notesEl=$("notes"), yrsEl=$("years"), tickEl=$("ticks");
  reserve(TX-640,TX+640,-1); reserve(XL-100,XF+330,-1); reserve(NEWF.x-330,XR,-1); reserve(NEWF.x-100,XR,1);
  /* proyectos: portadas, .flp y .als en dos carriles por lado; el carril exterior va intercalado para que su hilo pase entre los de dentro */
  const pre=["beat","untitled","new beat","loop","idea","bounce","trap","drill","melody","type beat","final","dark","hard","808 idea","keys","test","slow one","140bpm","asdfgh","rage","plugg","jerk idea"], suf=[""," 2"," v2"," v3"," (1)","_final"," new"," fix"," old"];
  const files=[]; const filesEl=$("files"); let cvi=0; const pad=n=>String(n).padStart(3,"0");
  function add(x,y,kind,size,cov,name){ const el=document.createElement("div"); el.className="file"; const up=y<0, hs=size/2;
    const img=kind==="cover"?`<img class="cv" src="assets/gcovers/cover-${cov}.jpg" alt="">`:`<img class="ic" src="assets/icons/${kind}.png" alt="">`;
    el.innerHTML=`<div class="stem" style="top:${up?hs+(name?50:8):-y+12}px;height:${Math.max(0,up?-y-hs-(name?64:22):y-hs-22)}px"></div><div class="box" style="left:${-hs}px;top:${-hs}px;width:${size}px;height:${size}px">${img}</div>${name?`<div class="nm" style="top:${hs+6}px">${name}</div>`:""}`;
    filesEl.appendChild(el); const f={el,x,y,kind,size,cov,ph:rnd()}; files.push(f); return f; }
  const target=add(TX,TY,"cover",CSZ,"023"); target.isTarget=true;
  add(XF,-300,"flp",230,null,"beat 1.flp");
  const free=(x,side)=>!zones.some(([a,b,s])=>s===side&&x>a-150&&x<b+150);
  for(const side of [-1,1]) for(const lane of [0,1]){ const y0=side<0?(lane?-900:-430):(lane?1010:540);
    for(let x=XL+640+(lane?210:0)+(side>0?105:0);x<=2380;x+=420){ const xx=x+(rnd()-.5)*40, size=190+rnd()*(lane?100:90), y=y0+(rnd()-.5)*50, k=rnd();
      const nm=pre[Math.floor(rnd()*pre.length)]+(rnd()<.35?" "+Math.floor(rnd()*140):"")+suf[Math.floor(rnd()*suf.length)];
      if(!free(xx,side))continue; if(k<.66){ let c; do{ c=pad(2+(cvi++%60)); }while(c==="023"); add(xx,y,"cover",size,c); } else add(xx,y,k<.9?"flp":"als",Math.min(size,210),null,nm+(k<.9?".flp":".als")); } }
  const newf=add(NEWF.x,NEWF.y,"flp",250,null,"bosque pero jerk.flp"); newf.isNew=true;
  /* las 28 portadas mas recientes son las que forman la rueda */
  const wheelItems=files.filter(f=>f.kind==="cover"&&!f.isTarget).sort((a,b)=>b.x-a.x).slice(0,28);
  wheelItems.forEach((f,j)=>{ f.fly=j; });
  /* THREE YEARS AGO sobre la portada */
  const tya=$("tya"), tyaS=[...tya.children]; tya.style.left=(TX-390)+"px"; tya.style.top=(TY-CSZ/2-70-3*203)+"px";
  /* Gallery */
  const gal=$("gal"); gal.style.left=(TX-540*GS)+"px"; gal.style.top=(TY-1070*GS)+"px"; gal.style.transform=`scale(${GS})`;
  const TAGC={trap:"#34C759",rnb:"#AF52DE",drill:"#FF3B30",dark:"#a3a3a3",melodic:"#007AFF",sample:"#FFCC00",jerk:"#FF9500",afro:"#5AC8FA",boombap:"#FF6482",lofi:"#8E8E93"};
  const BAR=["All","trap","rnb","drill","dark","melodic","sample","jerk","afro","boombap","lofi"];
  $("tagtrack").innerHTML=BAR.map((n,i)=>`<span class="tg" style="color:${i?`color-mix(in srgb,${TAGC[n]} 55%,#fff)`:"#f2f2f2"};font-weight:${i?400:700}">${n}</span>`).join("");
  $("gbtns").innerHTML=`<div class="gb" style="left:622px;width:76px"><svg viewBox="0 0 24 24" fill="none" stroke="#f2f2f2" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg></div><div class="gb" style="left:710px;width:76px"><svg viewBox="0 0 24 24" fill="none" stroke="#f2f2f2" stroke-width="2" stroke-linecap="round"><path d="M5 7h14M5 12h10M5 17h6"/></svg></div><div class="gb sel" style="left:798px;width:134px">Select</div><div class="gb" style="left:944px;width:76px"><svg viewBox="0 0 24 24" fill="none" stroke="#f2f2f2" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="10" r="3"/><path d="M6.5 18.5a6.5 6.5 0 0 1 11 0"/></svg></div>`;
  const nice=["Night Bus","Ruby","Static","Cold Brew","bosque","Gold Teeth","Blue Hour","Nylon","Mirage","Low Tide","Ember","Glass"], gcov=["006","011","017","018","023","041","024","026","027","035","039","045"], KEYS=["am","Bb","G","abm","Fm","C#m","Dm","Eb","F#m","Cm"], OT=["trap","drill","melodic","sample","jerk","afro","boombap","lofi","rnb","dark"];
  const colX=[200,540,880], ents=[]; const g2=mulberry(2511);
  for(let i=0;i<12;i++){ const tg=i===4?["melodic","dark"]:[OT[Math.floor(g2()*OT.length)]].concat(g2()<.5?[OT[Math.floor(g2()*OT.length)]]:[]); if(tg[1]===tg[0])tg.pop();
    const st=i===4?4:3+Math.floor(g2()*3), bk=i===4?"130 BPM":`${Math.round(82+g2()*88)} BPM · ${KEYS[Math.floor(g2()*KEYS.length)]}`;
    const el=document.createElement("div"); el.className="ent";
    el.innerHTML=`<div class="tile"><img src="assets/gcovers/cover-${gcov[i]}.jpg" alt=""></div><div class="ring"></div><div class="meta"><div class="title"><span>${nice[i]}</span><i>···</i></div><div class="detail"><div class="stars">${"★".repeat(st)}<s>${"★".repeat(5-st)}</s></div><div class="bk">${bk}</div></div><div class="tags">${tg.map(t=>`<span class="tag" style="color:${TAGC[t]};background:color-mix(in srgb,${TAGC[t]} 10%,transparent);border-color:color-mix(in srgb,${TAGC[t]} 32%,#2c2c2c)">${t}</span>`).join("")}</div></div>`;
    $("gents").appendChild(el); const x=colX[i%3], y=572+Math.floor(i/3)*498; ents.push({el,x,y,i,d:Math.hypot(x-540,y-1070),ring:el.querySelector(".ring")}); }
  const menu=$("menu"), mi0=$("mi0"), dim=$("dim"), splash=$("splash"), sbar=$("sbar");
  const MENU={x:598,y:1034};

  /* ---- camara: spline de Hermite con velocidades dadas (nunca se detiene hasta llegar a bosque) ---- */
  const K=[[0,2330,-500],[T.PASS0,TX+900,-2600],[T.PASS1,TX-700,-2300],[T.FIRST0,XF+820,-1500],[T.FIRST1,XF+90,-170],[T.TURN,XF+70,0],[T.BACK,TX,0]];
  function path(t){ if(t<=0)return K[0][1]; if(t>=T.BACK)return TX; let i=0; while(t>K[i+1][0])i++; const [t0,p0,m0]=K[i],[t1,p1,m1]=K[i+1],hh=t1-t0,s=(t-t0)/hh;
    return (2*s**3-3*s**2+1)*p0+(s**3-2*s**2+s)*hh*m0+(-2*s**3+3*s**2)*p1+(s**3-s**2)*hh*m1; }
  const C1={cx:path, cy:t=>kf(t,[[0,40],[T.TURN,40],[T.BACK,TY,E.ioC],[T.BACK+.1,TY],[T.GAL,TY-110*GS,E.ioC]]),
            z:t=>kf(t,[[0,.6],[T.PASS0,.55,E.ioS],[T.PASS1,.6,E.ioS],[T.FIRST1,.62,E.ioS],[T.BACK,.64,E.ioS],[T.BACK+.1,.64],[T.GAL,1/GS,E.ioC]])};
  const C5={cx:t=>kf(t,[[T.OUT,1750],[T.WH+1.1,150,E.ioS]]), cy:t=>kf(t,[[T.OUT,60],[T.WH+1.1,-40,E.ioS]]), z:t=>kf(t,[[T.OUT,.5],[T.WH+.5,.3,E.ioS]])};
  const cam=t=>{ const c=t<T.OLD+.3?C1:C5; return {cx:c.cx(t),cy:c.cy(t),z:c.z(t)}; };
  const toScreen=(x,y,t)=>{ const c=cam(t); return {x:540+(x-c.cx)*c.z,y:960+(y-c.cy)*c.z,z:c.z}; };
  let FE=null; const flyEnd=j=>FE?FE[j]:T.WH+.03+j*.019, flyStart=j=>(j===0&&FS0!==null)?FS0:flyEnd(j)-.55; let FS0=null;   // FE: llegada de cada portada a su pagina (la fija el rig)

  function frame(t){
    const s1=t<T.OLD+.15, s5=t>=T.OUT-.02;
    tl.style.visibility=(s1||s5)?"visible":"hidden"; if(!(s1||s5)){ menu.style.opacity=0; dim.style.opacity=0; splash.style.opacity=0; return; }
    const c=cam(t); w.style.transform=`translate(540px,960px) scale(${c.z.toFixed(5)}) translate(${(-c.cx).toFixed(2)}px,${(-c.cy).toFixed(2)}px)`;
    const vx=s1?(cam(t+1/60).cx-cam(t-1/60).cx)*30*c.z:0, mb=clamp((Math.abs(vx)-1500)/260,0,20);
    w.style.filter=mb>1.2?"url(#mb)":"none"; if(mb>1.2)mbfe.setAttribute("stdDeviation",`${(mb/c.z).toFixed(2)} 0`);
    /* al final: lo que no es portada se retira y la regla se recoge */
    const gone=s5?1-seg(t,T.WH-.75,T.WH-.5):1;
    ruler.style.opacity=(s5?1-seg(t,T.WH+.2,T.WH+.8):1).toFixed(3); tickEl.style.opacity=gone.toFixed(3); yrsEl.style.opacity=gone.toFixed(3); notesEl.style.opacity=gone.toFixed(3);
    /* THREE YEARS AGO */
    [HOOK.THREE,HOOK.YEARS,HOOK.AGO].forEach((t0,i)=>{ const u=seg(t,t0,t0+.13), o=s1&&t>=t0?1-seg(t,T.BACK+.12,T.BACK+.26):0; tyaS[i].style.opacity=o.toFixed(3);
      tyaS[i].style.transform=`scale(${(lerp(1.3,1,E.outC(u))+pulse(t,t0+.13,.03,14,30)).toFixed(4)})`; });
    /* proyectos */
    const gOn=s1&&t>=T.BACK-.03;
    for(const f of files){ let sc=1, op=1;
      if(f.isTarget&&gOn){ f.el.style.opacity=0; continue; }
      if(f.isNew){ if(!s5||t<T.OUT+.36){ f.el.style.opacity=0; continue; } sc=E.outB(seg(t,T.OUT+.36,T.OUT+.54)); }
      if(s5){ if(f.fly!==undefined){ if(t>=flyStart(f.fly)){ f.el.style.opacity=0; continue; } } else { const a=T.WH-.75+f.ph*.2; sc*=1-.5*E.inC(seg(t,a,a+.25)); op=1-seg(t,a,a+.25); } }
      f.el.style.opacity=op.toFixed(3); f.el.style.transform=`translate(${f.x.toFixed(1)}px,${f.y.toFixed(1)}px) scale(${sc.toFixed(4)})`; }
    /* Gallery: se abre alrededor de la portada, que no cambia */
    gal.style.visibility=gOn?"visible":"hidden";
    if(gOn){ const u=E.ioC(seg(t,T.BACK+.1,T.GAL-.04)), ins=(a)=>lerp(a,-2400,u).toFixed(0);
      gal.style.clipPath=`inset(${ins(918)}px ${ins(388)}px ${ins(698)}px ${ins(388)}px round ${lerp(14,0,u).toFixed(0)}px)`;
      for(const e of ents){ const a=T.BACK+.16+e.d*.0002, p=e.i===4?1:E.outB(seg(t,a,a+.26));
        e.el.style.opacity=e.i===4?1:seg(t,a,a+.1).toFixed(3); e.el.style.transform=`translate(${e.x}px,${e.y}px) scale(${(e.i===4?1+pulse(t,T.RCLICK,.03,12,24):.72+.28*p).toFixed(4)})`;
        if(e.i===4) e.ring.style.opacity=seg(t,T.RCLICK,T.RCLICK+.06).toFixed(3); } }
    /* menu contextual, velo y arranque de FL */
    const mo=t>=T.RCLICK&&t<T.SPLASH+.1?1-seg(t,T.OPEN+.05,T.SPLASH+.05):0; menu.style.opacity=mo.toFixed(3);
    menu.style.transform=`translate(${MENU.x}px,${MENU.y}px) scale(${(.6+.4*E.outB(seg(t,T.RCLICK+.01,T.RCLICK+.16))).toFixed(4)})`;
    mi0.style.background=t>=T.OPEN-.02?"#3d3d3d":`rgba(255,255,255,${(.1*seg(t,T.OPEN-.22,T.OPEN-.1)).toFixed(3)})`;
    dim.style.opacity=(s1?.62*seg(t,T.SPLASH-.02,T.SPLASH+.12)*(1-seg(t,T.OLD-.1,T.OLD+.04)):0).toFixed(3);
    const so=s1&&t>=T.SPLASH?1-seg(t,T.OLD-.06,T.OLD+.06):0; splash.style.opacity=so.toFixed(3);
    splash.style.transform=`scale(${(.82+.18*E.outB(seg(t,T.SPLASH,T.SPLASH+.16))+1.5*E.inC(seg(t,T.OLD-.14,T.OLD+.06))+pulse(t,T.NOTE1,.014,12,26)+pulse(t,T.NOTE2,.018,12,26)).toFixed(4)})`;
    sbar.style.transform=`scaleX(${E.ioS(seg(t,T.SPLASH+.04,T.OLD-.14)).toFixed(4)})`;
  }
  return {frame,toScreen,cam,MENU,NEWF,wheelItems,flyStart,flyEnd,setFly(a){FE=a;},setLeadStart(t){FS0=t;},measure(){}};
})();
