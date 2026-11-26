/* Escritorio: Finder (escena 2) -> Gallery de BeatGaler, tags, seleccion, Quick Pack y link (escena 3).
   Finder, cursor, mutacion archivo->portada y barra de tags vienen de add-finder; aqui se recomponen para vertical.
   Coordenadas de capa = 1080x1920 sin camara. */
const DESK=(function(){
  const root=$("sDesk"), LISTTOP=436, ROWH=64, N=24, K=150;
  const rnd=mulberry(2511), rndF=mulberry(77);
  const TAGC={trap:"#34C759",rnb:"#AF52DE",drill:"#FF3B30",dark:"#a3a3a3",melodic:"#007AFF",sample:"#FFCC00",jerk:"#FF9500",afro:"#5AC8FA",boombap:"#FF6482",lofi:"#8E8E93"};
  const BAR=["All","trap","rnb","drill","dark","melodic","sample","jerk","afro","boombap","lofi"];
  const MON=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  const pre=["beat","untitled","new beat","loop","idea","project","bounce","mix","trap","drill","melody","sample flip","type beat","final","beat_final","dark","hard","808 idea","keys","test","rnb sketch","slow one","140bpm","asdfgh"], suf=[""," 2"," v2"," v3"," (1)"," (2)","_final"," FINAL"," new"," b"," fix"," old"];
  const nice=["Night Bus","Ruby","Static","Cold Brew","Velvet","Gold Teeth","Blue Hour","Nylon","Mirage","Low Tide","Ember","Glass","Motel","After Hours","Soft Focus","Neon Rain","Halo","Dust","Marble","Fever","Polaroid","Ghost Lane","Honey","Chrome"];
  const KEYS=["am","Bb","G","abm","Fm","C#m","Dm","Eb","F#m","Cm"];
  const pool=["006","011","017","018","022","041","024","026","027","035","039","045","048","053","010","002","029","033","038","055","059"];
  const PICK={4:"031",9:"023",13:"034"}, RNB=[1,4,6,9,13,16,20], DARKONLY=[2,11,18], OTHER=["trap","drill","melodic","sample","jerk","afro","boombap","lofi"];
  root.innerHTML=`<div id="dcam">
    <div class="fwin ghost" id="fg1"><div class="f-title"><div class="f-dots"><i style="background:#ee6a5f"></i><i style="background:#f5bd4f"></i><i style="background:#61c454"></i></div><div class="f-name">Beats 2025</div></div><div class="f-cols"></div><div class="f-list"></div><div class="f-foot">1,204 items</div></div>
    <div class="fwin ghost" id="fg2"><div class="f-title"><div class="f-dots"><i style="background:#ee6a5f"></i><i style="background:#f5bd4f"></i><i style="background:#61c454"></i></div><div class="f-name">old beats</div></div><div class="f-cols"></div><div class="f-list"></div><div class="f-foot">632 items</div></div>
    <div class="fwin" id="finder"><div class="f-title"><div class="f-dots"><i style="background:#ee6a5f"></i><i style="background:#f5bd4f"></i><i style="background:#61c454"></i></div><div class="f-name">Beats</div></div>
      <div class="f-cols"><span style="left:92px">Name</span><span style="left:520px">Date Modified</span><span style="left:770px">Size</span></div>
      <div class="f-list"><div class="f-rows" id="f-rows"></div><div class="f-thumb" id="f-thumb"></div></div><div class="f-foot" id="f-foot">847 items</div></div>
    <div id="tagbar"><div id="tagtrack"></div></div>
    <div id="gents"></div>
    <div id="gbtns">
      <div class="gb" style="left:622px;width:76px"><svg viewBox="0 0 24 24" fill="none" stroke="#f2f2f2" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg></div>
      <div class="gb" style="left:710px;width:76px"><svg viewBox="0 0 24 24" fill="none" stroke="#f2f2f2" stroke-width="2" stroke-linecap="round"><path d="M5 7h14M5 12h10M5 17h6"/></svg></div>
      <div class="gb sel" id="gsel" style="left:798px;width:134px">Select</div>
      <div class="gb" style="left:944px;width:76px"><svg viewBox="0 0 24 24" fill="none" stroke="#f2f2f2" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="10" r="3"/><path d="M6.5 18.5a6.5 6.5 0 0 1 11 0"/></svg></div>
    </div>
    <div id="selbar"><div class="cnt"><b id="selcnt">0</b><span>selected</span></div><div class="btn" id="packbtn">Create pack</div></div>
    <div id="gdim"></div>
    <div id="sheet"><div class="lab">Quick Pack</div><div class="ttl">dark rnb pack</div><div class="sub">3 beats · anyone with the link can listen</div>
      <div class="field"><b>beatgaler.com/p/</b>dark-rnb</div><div class="copy" id="copybtn">Copy link</div></div>
    <div id="flys"></div>
  </div>`;
  const cam=$("dcam"), finder=$("finder"), fg1=$("fg1"), fg2=$("fg2"), rowsEl=$("f-rows"), thumb=$("f-thumb"), foot=$("f-foot"), fe=$("vb2fe");
  const gents=$("gents"), tagbar=$("tagbar"), track=$("tagtrack"), gbs=[...root.querySelectorAll(".gb")], gsel=$("gsel"), selbar=$("selbar"), selcnt=$("selcnt"), packbtn=$("packbtn"), gdim=$("gdim"), sheet=$("sheet"), copybtn=$("copybtn"), flys=$("flys");
  /* ---- filas del Finder ---- */
  const rows=[];
  for(let r=0;r<K;r++){
    const tr=rndF(), type=tr<.42?"wav":tr<.62?"mp3":tr<.81?"flp":"als";
    const nm=pre[Math.floor(rndF()*pre.length)]+(rndF()<.45?" "+Math.floor(rndF()*140):"")+suf[Math.floor(rndF()*suf.length)]+"."+type;
    const row=document.createElement("div"); row.className="row"+(r%2?" alt":""); row.style.top=(r*ROWH)+"px";
    row.innerHTML=`<div class="bg"></div>${(window.FILE_ICONS&&(type==="flp"||type==="als"))?`<img class="ico ico2" src="assets/icons/${type}.png" alt="">`:`<div class="ico ${type==="mp3"?"mp3":type==="flp"?"prj":type==="als"?"prj2":""}"></div>`}<div class="txt"><span class="n">${nm}</span><span class="d">${MON[Math.floor(rndF()*12)]} ${1+Math.floor(rndF()*27)}, 2026</span><span class="s">${(18+rndF()*52).toFixed(1)} MB</span></div>`;
    rowsEl.appendChild(row); rows.push({row,ri:r,bg:row.querySelector(".bg"),txt:row.querySelector(".txt"),ico:row.querySelector(".ico"),nm,type});
  }
  // dos golpes de scroll con inercia (curva validada en add-finder); el cursor nunca se mueve mientras hay scroll
  const inert=u=>(1-Math.exp(-5.2*Math.pow(u,1.25)))/(1-Math.exp(-5.2));
  const SC0=320, D1=2432, D2=4608, SCEND=SC0+D1+D2, R0=SCEND/ROWH; // R0 = primera fila visible al final (115)
  const F={IN:HOOK.WHIP+.02, S1a:B+.10, S1b:B+1.05, S2a:W.HUNDREDS+.03, S2b:W.HUNDREDS+.98, ZOOM:B+2.70};
  const scrollAt=t=>SC0+D1*inert(seg(t,F.S1a,F.S1b))+D2*inert(seg(t,F.S2a,F.S2b));
  /* ---- beats ---- */
  const colX=[200,540,880], slotPos=k=>({x:colX[k%3], y:572+Math.floor(k/3)*498});
  const ents=[]; let pq=0;
  for(let i=0;i<N;i++){
    const tags=RNB.includes(i)?(PICK[i]?["rnb","dark"]:["rnb",OTHER[Math.floor(rnd()*4)]]):DARKONLY.includes(i)?["dark",OTHER[Math.floor(rnd()*OTHER.length)]]:[OTHER[Math.floor(rnd()*OTHER.length)]].concat(rnd()<.5?[OTHER[Math.floor(rnd()*OTHER.length)]]:[]);
    if(tags[1]===tags[0])tags.pop();
    const cover=PICK[i]||pool[pq++], vi=i<20?i:[2,7,11,16][i-20], src=rows[R0+vi];
    const bpm=Math.round(82+rnd()*88), key=KEYS[Math.floor(rnd()*KEYS.length)], stars=PICK[i]?5:3+Math.floor(rnd()*3);
    const el=document.createElement("div"); el.className="ent";
    const bars=[60,120,84,150,96,56].map(h=>`<b style="height:${h}px"></b>`).join("");
    el.innerHTML=`<div class="tile"><div class="lite"></div>${(window.FILE_ICONS&&(src.type==="flp"||src.type==="als"))?`<img class="ficon" src="assets/icons/${src.type}.png" alt="">`:`<div class="glyph">${bars}</div>`}<img class="cov" src="assets/covers/cover-${cover}.jpg" alt=""><div class="sheen"></div><div class="flash"></div></div>
      <div class="ring"></div><div class="chk"><svg viewBox="0 0 24 24" fill="none" stroke="#0c0c0c" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>
      <div class="meta"><div class="title"><span>${nice[i]}</span><i>···</i></div>
      <div class="detail"><div class="stars">${"<s>★</s>".repeat(5)}</div><div class="bk">${bpm} BPM · ${key}</div></div>
      <div class="tags">${tags.map(t=>`<span class="tag" style="color:${TAGC[t]};background:color-mix(in srgb,${TAGC[t]} 10%,transparent);border-color:color-mix(in srgb,${TAGC[t]} 32%,#2c2c2c)">${t}</span>`).join("")}</div></div>`;
    gents.appendChild(el);
    const q=s=>el.querySelector(s);
    const s1=RNB.indexOf(i), s2=PICK[i]?Object.keys(PICK).map(Number).indexOf(i):-1;
    ents.push({i,el,tags,cover,vi,src,stars,s0:slotPos(i),s1:s1>=0?slotPos(s1):null,s2:s2>=0?slotPos(s2):null,pick:s2,
      tile:q(".tile"),img:q("img.cov"),glyph:q(".glyph")||q(".ficon"),lite:q(".lite"),flash:q(".flash"),sheen:q(".sheen"),ring:q(".ring"),chk:q(".chk"),chkS:q(".chk svg"),meta:q(".meta"),
      title:q(".title"),starEls:[...el.querySelectorAll(".stars s")],bk:q(".bk"),tagEls:[...el.querySelectorAll(".tag")],
      x0:135+(i>=20?60:0), y0:LISTTOP+vi*ROWH+32, launch:S.TAKE+Math.min(.5,i*.02+rnd()*.03),
      swx:(rnd()-.5)*1050, swy:(rnd()-.5)*1500, swz:-650+rnd()*1250, sph:rnd()*6.28, swr:.5+rnd()*1.1, rz:(rnd()-.5)*150, rx:(rnd()-.5)*110, ry:(rnd()-.5)*130,
      bloom:S.LAND-1.0+Math.floor(rnd()*5)*.2+rnd()*.06, info:S.LAND+.02+rnd()*.2, fd:rnd()*.08});
  }
  const picks=ents.filter(e=>e.pick>=0).sort((a,b)=>a.pick-b.pick);
  // portadas que vuelan de las tarjetas a la hoja del pack
  const FAN=[{x:372,y:660,r:-9,s:1},{x:540,y:630,r:0,s:1.14},{x:708,y:660,r:9,s:1}];
  const fl=picks.map((e,k)=>{const d=document.createElement("div");d.className="fly";d.innerHTML=`<img src="assets/covers/cover-${e.cover}.jpg" alt="">`;d.style.zIndex=k===1?3:2;flys.appendChild(d);return d;});
  /* ---- barra de tags real ---- */
  BAR.forEach(n=>{const p=document.createElement("span");p.className="tg";p.textContent=n;p.style.fontWeight=700;track.appendChild(p);});
  const tgEls=[...track.children]; let tagX=null;
  function measureTags(){ tgEls.forEach(p=>{p.style.width="auto";p.style.fontWeight=700;}); tgEls.forEach(p=>{p.style.width=Math.ceil(p.offsetWidth)+"px";p.style.fontWeight=400;});
    tagX={}; tgEls.forEach((p,k)=>{tagX[BAR[k]]=58+p.offsetLeft+p.offsetWidth/2;}); }
  measureTags(); let fontOK=false;
  const idleCol=c=>c?`color-mix(in srgb,${c} 55%,#fff)`:"#828282";
  /* ---- tipografia ---- */
  const HUN=[0,1,2].map(()=>KW("HUNDREDS",740,{ink:true})), ONE1=KW("ONE",420,{ink:true}), BY=KW("BY",278,{ink:true}), ONE2=KW("ONE",420,{ink:true});
  const PACKS=KW("PACKS",760), READY=KW("READY",760), ORG=KW("ORGANIZE",840), GENRE=KW("GENRE",600), MOOD=KW("MOOD",560);
  const chip=document.createElement("div"); chip.id="chip"; chip.textContent="beatgaler.com/p/dark-rnb"; $("kt").appendChild(chip);
  /* ---- camara ---- */
  const T=S;
  function camAt(t){
    const k=(a)=>kf(t,a);
    const fx=k([[0,540],[F.ZOOM,540],[F.ZOOM+.45,360,E.ioC],[T.TAKE-.3,360],[T.TAKE,540,E.ioC],[99,540]]);
    const fy=k([[0,1030],[F.ZOOM,1030],[F.ZOOM+.45,756,E.ioC],[T.TAKE-.3,756],[T.TAKE,1030,E.ioC],[T.TAKE+.5,1000,E.outC],[T.LAND,960,E.ioC],[11.0+M,960],[12.2+M,330,E.ioC],[T.TAG2+.05,330],[T.TAG2+.36,700,E.ioC],[T.PACK,700],[T.PACK+.3,865,E.ioC],[99,865]]);
    let s=k([[0,1.0],[F.S2a,1.07,E.lin],[F.S2a+.3,.84,E.outC],[F.ZOOM,.87,E.lin],[F.ZOOM+.45,1.42,E.ioC],[T.TAKE-.3,1.46,E.lin],[T.TAKE,1.0,E.ioC],[T.TAKE+.5,.8,E.outC],[T.LAND,.86,E.ioC],[11.0+M,.88,E.lin],[12.2+M,1.06,E.ioC],[T.TAG2+.05,1.07,E.lin],[T.TAG2+.36,1.06,E.ioC],[T.PACK,1.08,E.lin],[T.PACK+.3,1.1,E.ioC],[T.BACK,1.13,E.lin],[99,1.13]]);
    const sx=k([[0,540],[F.ZOOM,540],[F.ZOOM+.45,480,E.ioC],[T.TAKE-.3,480],[T.TAKE,540,E.ioC],[99,540]]);
    let sy=k([[0,1030],[F.ZOOM,1010],[F.ZOOM+.45,640,E.ioC],[T.TAKE-.3,640],[T.TAKE,1030,E.ioC],[T.TAKE+.5,980,E.outC],[T.LAND,1010,E.ioC],[11.0+M,1010],[12.2+M,560,E.ioC],[T.TAG2+.05,560],[T.TAG2+.36,860,E.ioC],[T.PACK,860],[T.PACK+.3,900,E.ioC],[99,900]]);
    const rx=k([[0,0],[T.TAKE,0],[T.TAKE+.55,13,E.outC],[T.LAND,0,E.ioC],[99,0]]);
    const rz=k([[0,0],[T.TAKE,0],[T.TAKE+.45,-5,E.outC],[T.LAND-.4,2,E.ioS],[T.LAND,0,E.ioS],[99,0]]);
    s*=1+pulse(t,T.LAND,.022,10,24)+pulse(t,T.TAG1,.012,12,24)+pulse(t,T.TAG2,.012,12,24)+pulse(t,T.PACK,.014,12,24)+pulse(t,T.COPY,.014,12,24)+pulse(t,W.HUNDREDS,.012,12,24);
    sy+=(1-E.outC(seg(t,F.IN,F.IN+.36)))*2300;
    const out=E.inC(seg(t,T.BACK-.04,T.BACK+.24));
    return {fx,fy,s,sx:sx-out*1700,sy,rx,rz,ry:out*-18,blur:out*10+(t<F.IN+.3?(1-seg(t,F.IN,F.IN+.3))*8:0)};
  }
  const setCam=c=>{cam.style.transform=`translate3d(${c.sx.toFixed(2)}px,${c.sy.toFixed(2)}px,0) rotateY(${(c.ry||0).toFixed(2)}deg) rotateX(${c.rx.toFixed(2)}deg) rotateZ(${c.rz.toFixed(2)}deg) scale(${c.s.toFixed(4)}) translate(${(-c.fx).toFixed(2)}px,${(-c.fy).toFixed(2)}px)`; cam.style.filter=c.blur>.3?`blur(${c.blur.toFixed(1)}px)`:"none";};
  const toS=(t,x,y)=>{const c=camAt(t); return {x:c.sx+(x-c.fx)*c.s, y:c.sy+(y-c.fy)*c.s};};
  /* ---- cursor: guion de movimientos ---- */
  const hov=[R0+3,R0+5,R0+8,R0+3,R0+5,R0+7]; // filas que examina
  const rowY=r=>LISTTOP+(r-R0)*ROWH+32;
  function buildCursor(){
    const P=[], C=[]; const at=(tc,x,y)=>toS(tc,x,y);
    const a0=toS(B+1.4,330,rowY(hov[0])-0), a1=toS(B+1.6,350,rowY(hov[1]));
    P.push([F.IN+.05,F.IN+.4,830,1340]);
    // tras el primer scroll (la fila queda donde termino el scroll 1): duda entre dos archivos
    P.push([B+1.02,B+1.34,330,790],[B+1.44,B+1.70,372,918]);
    // uno por uno, con la camara cerca
    const z1=at(F.ZOOM+.6,330,rowY(hov[3])), z2=at(F.ZOOM+.6,372,rowY(hov[4])), z3=at(F.ZOOM+.6,340,rowY(hov[5]));
    P.push([W.ONE1-.34,W.ONE1-.02,z1.x,z1.y],[W.BY-.26,W.BY+.0,z2.x,z2.y],[W.ONE2+.08,W.ONE2+.36,z3.x,z3.y],[T.TAKE-.14,T.TAKE+.2,1180,1500]);
    // Gallery
    const g1=at(T.TAG1,tagX.rnb,338), g2=at(T.TAG2,tagX.dark,338), g3=at(T.SEL0,866,474), c1=at(T.SEL1,230,610), c2=at(T.SEL2,570,610), c3=at(T.SEL3,910,610), pb=at(T.PACK,812,1076), cb=at(T.COPY,540,1206);
    P.push([12.02+M,12.03+M,1180,g1.y+260],[12.06+M,12.52+M,g1.x,g1.y+6],[T.TAG1+.18,T.TAG2-.26,g2.x,g2.y+6],[T.TAG2+.1,T.SEL0-.14,g3.x,g3.y+6],[T.SEL0+.14,T.SEL1-.2,c1.x,c1.y],[T.SEL1+.1,T.SEL2-.1,c2.x,c2.y],[T.SEL2+.1,T.SEL3-.1,c3.x,c3.y],[T.SEL3+.08,T.PACK-.12,pb.x,pb.y+6],[T.PACK+.14,T.COPY-.16,cb.x,cb.y+6],[T.COPY+.2,T.BACK,cb.x+420,cb.y+500]);
    C.push(T.TAG1,T.TAG2,T.SEL0,T.SEL1,T.SEL2,T.SEL3,T.PACK,T.COPY);
    CURSOR.path=P; CURSOR.clicks=C; CURSOR.vis=[[F.IN+.05,T.TAKE+.2],[12.03+M,T.BACK]];
  }
  buildCursor();
  const SELT=[T.SEL1,T.SEL2,T.SEL3];
  function frame(t){
    const on=t>F.IN-.02&&t<T.BACK+.3; root.style.visibility=on?"visible":"hidden";
    if(!on){ [...HUN,ONE1,BY,ONE2,PACKS,READY,ORG,GENRE,MOOD].forEach(w=>w.put(0,0,{o:0})); chip.style.opacity=0; if(t<F.IN||t>T.BACK+.3){ $("cursor").style.opacity=0; } return; }
    if(!fontOK&&KT.ready){ measureTags(); buildCursor(); fontOK=true; }
    const c=camAt(t); setCam(c);
    /* ===== Finder ===== */
    const finderOn=t<T.TAKE+.75; finder.style.visibility=finderOn?"visible":"hidden";
    const gOn=t>W.HUNDREDS-.02&&t<F.ZOOM+.5; fg1.style.visibility=fg2.style.visibility=gOn?"visible":"hidden";
    const scroll=scrollAt(t), sv=Math.abs(vel(scrollAt,t));
    if(finderOn){
      rowsEl.style.transform=`translateY(${(-scroll).toFixed(2)}px)`;
      fe.setAttribute("stdDeviation","0 "+Math.min(30,sv/240).toFixed(1)); rowsEl.style.filter=sv>300?"url(#vb2)":"none";
      foot.textContent=Math.round(lerp(212,847,E.outC(seg(t,F.S1a,F.S2b))))+" items";
      thumb.style.transform=`translateY(${(scroll/(K*ROWH)*1200+30).toFixed(1)}px)`;
      const fo=seg(t,T.TAKE+.2,T.TAKE+.7); finder.style.opacity=(1-fo).toFixed(3);
      finder.style.transform=`translate3d(0,${(fo*120).toFixed(1)}px,${(-fo*500).toFixed(1)}px) scale(${(1-fo*.06).toFixed(4)})`;
      if(gOn){ const g=E.outC(seg(t,W.HUNDREDS,W.HUNDREDS+.3))*(1-seg(t,F.ZOOM,F.ZOOM+.4));
        fg1.style.transform=`translate3d(${(-470*g).toFixed(1)}px,${(-150*g).toFixed(1)}px,-260px) rotateZ(${(-5*g).toFixed(2)}deg)`; fg2.style.transform=`translate3d(${(480*g).toFixed(1)}px,${(90*g).toFixed(1)}px,-420px) rotateZ(${(4.5*g).toFixed(2)}deg)`;
        fg1.style.filter="blur(5px) brightness(.72)"; fg2.style.filter="blur(8px) brightness(.6)"; fg1.style.opacity=fg2.style.opacity=Math.min(1,g*3).toFixed(3);
        fg1.querySelector(".f-list").style.backgroundPositionY=fg2.querySelector(".f-list").style.backgroundPositionY=(-scroll*.8).toFixed(0)+"px"; }
      // resaltado de la fila bajo el dedo
      const cp=CURSOR.pos(t), ly=c.fy+(cp.y-c.sy)/c.s, hOn=(t>B+1.0&&t<T.TAKE-.1&&sv<200)?1:0;
      const first=Math.max(0,Math.floor(scroll/ROWH)-2), last=Math.min(K-1,first+26);
      for(let r=first;r<=last;r++){ const f=rows[r], fy=LISTTOP+r*ROWH-scroll+32;
        f.bg.style.opacity=(hOn*clamp(1-Math.abs(fy-ly)/ROWH,0,1)*.2).toFixed(3); }
    }
    /* ===== beats: archivo -> portada -> BeatCard -> filtros -> seleccion ===== */
    const sel=SELT.map(ts=>t>=ts), nsel=sel.filter(Boolean).length;
    for(const e of ents){
      const L=e.launch, flown=t>=L;
      if(finderOn){ const gone=seg(t,L,L+.16); e.src.txt.style.opacity=(1-gone).toFixed(3); e.src.txt.style.transform=`translateX(${(gone*46).toFixed(1)}px)`; e.src.ico.style.opacity=flown?0:1; }
      if(!flown){ e.el.style.opacity=0; continue; }
      const u=seg(t,L,T.LAND), hump=Math.sin(Math.PI*Math.pow(u,.8));
      let x,y,z=0,s=1,rz=e.rz*hump*(1-u*.3),rx=e.rx*hump,ry=e.ry*hump,op=1,blur=0,bright=1;
      if(u<1){ const a=E.outC(seg(u,0,.34)), b=Math.pow(seg(u,.52,1),2.3), ang=e.sph+u*2.4*e.swr, wob=60*hump;
        const fx=540+e.swx+Math.cos(ang)*wob, fy=930+e.swy+Math.sin(ang)*wob;
        x=lerp(lerp(e.x0,fx,a),e.s0.x,b); y=lerp(lerp(e.y0,fy,a),e.s0.y,b); z=lerp(e.swz*a,0,b);
        s=lerp(.14,.86,E.outB(Math.min(1,u/.3)))+.14*b;
        blur=a*(1-b)*clamp(Math.abs(z-150)/800*10,0,11); bright=1-.35*a*(1-b)*clamp((150-z)/900,0,1);
      } else { x=e.s0.x; y=e.s0.y; }
      s*=1+pulse(t,T.LAND,.09,10,27)+pulse(t,e.bloom,.1,13,28)+pulse(t,e.info,.03,14,26); y+=pulse(t,T.LAND,22,9,21);
      // filtros: los que coinciden se recolocan, los demas se apagan
      if(t>=T.TAG1){ const d=e.fd, q1=E.ioC(seg(t,T.TAG1+.05+d,T.TAG1+.45+d));
        if(e.s1){ x=lerp(e.s0.x,e.s1.x,q1); y=lerp(e.s0.y,e.s1.y,q1);
          if(t>=T.TAG2){ const q2=E.ioC(seg(t,T.TAG2+.05+d,T.TAG2+.45+d));
            if(e.s2){ x=lerp(e.s1.x,e.s2.x,q2); y=lerp(e.s1.y,e.s2.y,q2); s*=1+pulse(t,T.TAG2+.45+d,.04,13,26); }
            else { const g=seg(t,T.TAG2+d,T.TAG2+.2+d); op=1-g; s*=1-.3*E.inQ(g); } }
          else s*=1+pulse(t,T.TAG1+.45+d,.04,13,26);
        } else { const g=seg(t,T.TAG1+d,T.TAG1+.2+d); op=1-g; s*=1-.3*E.inQ(g); } }
      if(op<=.001){ e.el.style.opacity=0; continue; }
      // seleccion
      if(e.pick>=0){ const ts=SELT[e.pick], on=t>=ts, mode=E.outC(seg(t,T.SEL0+.02+e.pick*.04,T.SEL0+.2+e.pick*.04));
        e.chk.style.opacity=mode.toFixed(3); e.chk.className="chk"+(on?" on":""); e.chkS.style.opacity=on?1:0;
        e.chk.style.transform=`scale(${((.5+.5*mode)*(1+pulse(t,ts,.3,12,24))).toFixed(3)})`;
        e.ring.style.opacity=on?1:0; e.ring.style.transform=`scale(${(on?1+.06*Math.exp(-(t-ts)*14):1).toFixed(4)})`;
        s*=1-pulse(t,ts,.05,12,26);
      }
      e.el.style.opacity=op.toFixed(3);
      e.el.style.transform=`translate3d(${x.toFixed(2)}px,${y.toFixed(2)}px,${z.toFixed(2)}px) rotateZ(${rz.toFixed(2)}deg) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) scale(${s.toFixed(4)})`;
      let fl=""; if(blur>.35)fl+=`blur(${blur.toFixed(1)}px) `; if(bright<.99)fl+=`brightness(${bright.toFixed(3)})`; e.el.style.filter=fl||"none";
      const dk=seg(t,T.LAND-.35,T.LAND-.1); e.lite.style.opacity=(1-dk).toFixed(3); e.glyph.style.color=dk<.5?"#66666d":"#96969c";
      const bt=e.bloom, gu=seg(t,bt,bt+.2), bu=gu<=0?0:E.outB(gu);
      e.img.style.opacity=gu>0?1:0; e.img.style.transform=`scale(${Math.max(.02,bu).toFixed(4)})`; e.img.style.borderRadius=`${(50*(1-E.outC(seg(gu,.3,.9)))).toFixed(1)}%`;
      e.flash.style.opacity=(t>=bt?.45*Math.exp(-(t-bt)*17):0).toFixed(3);
      e.glyph.style.opacity=(1-seg(gu,.3,.7)).toFixed(3);
      const su=seg(t,bt+.04,bt+.42); e.sheen.style.opacity=(su>0&&su<1?Math.sin(Math.PI*su):0).toFixed(3); e.sheen.style.transform=`translateX(${(-170+su*520).toFixed(1)}px)`;
      const iu=t-e.info, tu=E.outC(seg(iu,0,.12));
      e.title.style.opacity=tu.toFixed(3); e.title.style.transform=`translateY(${((1-tu)*14).toFixed(1)}px)`;
      for(let k=0;k<5;k++){const a=seg(iu,.03+k*.018,.08+k*.018); e.starEls[k].style.color=(k<e.stars&&a>.5)?"#d4d4d4":"#454545"; e.starEls[k].style.opacity=seg(iu,.02,.08).toFixed(3); e.starEls[k].style.transform=`scale(${(1+(k<e.stars?Math.sin(Math.PI*a)*.45:0)).toFixed(3)})`;}
      e.bk.style.opacity=E.outC(seg(iu,.06,.16)).toFixed(3);
      e.tagEls.forEach((tg,k)=>{const a=seg(iu,.1+k*.03,.2+k*.03); tg.style.opacity=Math.min(1,a*2).toFixed(3); tg.style.transform=`scale(${(a<=0?.6:E.outB(a)*.4+.6).toFixed(3)})`;});
    }
    /* ===== barra de tags, botones, barra de seleccion ===== */
    const inc1=t>=T.TAG1, inc2=t>=T.TAG2;
    tgEls.forEach((p,k)=>{ const a=E.outC(seg(t,T.LAND+.05+k*.025,T.LAND+.27+k*.025)); p.style.opacity=a.toFixed(3); p.style.transform=`translateX(${((1-a)*70).toFixed(1)}px)`;
      const n=BAR[k], on=(n==="rnb"&&inc1)||(n==="dark"&&inc2), tc=n==="rnb"?T.TAG1:T.TAG2;
      if(k===0){ p.style.color=inc1?"#9b9b9b":"#f4f4f4"; p.style.fontWeight=inc1?400:700; }
      else if(on){ p.style.color=n==="dark"?"#f4f4f4":TAGC[n]; p.style.fontWeight=700; p.style.textShadow=`0 0 ${(26*Math.exp(-(t-tc)*5)).toFixed(0)}px currentColor`; p.style.transform=`scale(${(1+pulse(t,tc,.12,12,24)).toFixed(4)})`; }
      else { p.style.color=idleCol(n==="dark"?null:TAGC[n]); p.style.fontWeight=400; p.style.textShadow="none"; } });
    gbs.forEach((b,k)=>{ const a=E.outB(seg(t,T.LAND+.12+k*.04,T.LAND+.4+k*.04)); b.style.opacity=Math.min(1,a*1.5).toFixed(3); b.style.transform=`scale(${(.6+.4*a).toFixed(3)})`; });
    const sm=t>=T.SEL0; gsel.style.background=sm?"#f5f5f5":""; gsel.style.color=sm?"#0c0c0c":""; gsel.style.transform=`scale(${(1-pulse(t,T.SEL0,.1,12,24)).toFixed(4)})`;
    const sb=E.outB(seg(t,T.SEL0+.03,T.SEL0+.33)); selbar.style.opacity=Math.min(1,sb*2).toFixed(3); selbar.style.transform=`translateY(${((1-sb)*150).toFixed(1)}px)`;
    selcnt.textContent=nsel; packbtn.style.opacity=nsel?1:.35; packbtn.style.transform=`scale(${(1+pulse(t,SELT[2],.05,12,24)-pulse(t,T.PACK,.1,12,24)).toFixed(4)})`;
    /* ===== hoja del Quick Pack ===== */
    const sh=seg(t,T.PACK+.02,T.PACK+.3), shb=sh<=0?0:E.outB(sh);
    gdim.style.opacity=(.72*E.outC(seg(t,T.PACK,T.PACK+.25))).toFixed(3);
    sheet.style.opacity=Math.min(1,sh*3).toFixed(3); sheet.style.transform=`translateY(${((1-shb)*160).toFixed(1)}px) scale(${(.86+.14*shb).toFixed(4)})`;
    fl.forEach((d,k)=>{ const e=picks[k], q=E.ioC(seg(t,T.PACK+k*.04,T.PACK+.36+k*.04)), f=FAN[k];
      d.style.opacity=t>=T.PACK?1:0; const hp=Math.sin(Math.PI*q);
      d.style.transform=`translate3d(${lerp(e.s2.x,f.x,q).toFixed(2)}px,${(lerp(e.s2.y,f.y,q)-hp*70).toFixed(2)}px,${(hp*160).toFixed(1)}px) rotate(${(f.r*q+hp*(k-1)*-14).toFixed(2)}deg) scale(${(lerp(304/220,f.s,q)*(1+pulse(t,T.PACK+.36+k*.04,.06,13,26)+pulse(t,T.COPY,.04,12,24))).toFixed(4)})`; });
    const cp2=t>=T.COPY; copybtn.textContent=cp2?"Link copied":"Copy link"; copybtn.style.background=cp2?"#34C759":"#f5f5f5"; copybtn.style.color=cp2?"#fff":"#0c0c0c"; copybtn.style.transform=`scale(${(1-pulse(t,T.COPY,.07,12,24)).toFixed(4)})`;
    /* ===== tipografia ===== */
    HUN.forEach((w,k)=>{ const t0=W.HUNDREDS+k*.07, sl=slam(t,t0), out=E.inC(seg(t,F.ZOOM-.12+k*.03,F.ZOOM+.12+k*.03));
      w.put(540,610+k*w.h*1.02-out*1700,{o:sl.o*(out<1?1:0),s:sl.s,by:out>0?50:sl.b}); });
    const o3=E.inC(seg(t,T.TAKE-.1,T.TAKE+.12));
    [[ONE1,W.ONE1,0],[BY,W.BY,1],[ONE2,W.ONE2,2]].forEach(([w,t0,k])=>{ const sl=slam(t,t0,.1); w.put(120+w.w/2+o3*-1300,1120+k*188,{o:sl.o*(o3<1?1:0),s:sl.s,by:sl.b,b:o3*12}); });
    const o4=E.inC(seg(t,T.LAND+.3,T.LAND+.5));
    [[PACKS,W.PACKS,0],[READY,W.READY1,1]].forEach(([w,t0,k])=>{ const sl=slam(t,t0,.13); w.put(540,760+k*w.h*1.02-o4*1500,{o:sl.o*(o4<1?1:0),s:sl.s*(1+(t-t0)*.03),by:o4>0?50:sl.b}); });
    const typeY=tb=>{ const p=toS(t,540,300); return p.y-tb; };
    { const sl=slam(t,W.ORGANIZE,.13), out=E.inC(seg(t,W.GENRE-.3,W.GENRE-.12)); ORG.put(540,typeY(30+ORG.h/2)-out*700,{o:sl.o*(out<1?1:0),s:sl.s,by:out>0?40:sl.b}); }
    { const sl=slam(t,W.GENRE,.12), out=E.inC(seg(t,W.MOOD-.16,W.MOOD-.02)); GENRE.put(120+GENRE.w/2-out*900,typeY(34+GENRE.h/2),{o:sl.o*(out<1?1:0),s:sl.s,by:sl.b,b:out*12}); }
    { const sl=slam(t,W.MOOD,.12), out=E.inC(seg(t,T.TAG2+.28,T.TAG2+.44)); MOOD.put(960-MOOD.w/2+out*900,typeY(34+MOOD.h/2),{o:sl.o*(out<1?1:0),s:sl.s,by:sl.b,b:out*12}); }
    /* ===== el link sale de la hoja ===== */
    if(t>=T.COPY+.06&&t<T.BACK){ const p0=toS(T.COPY,420,1080), q=E.outC(seg(t,T.COPY+.06,T.COPY+.36));
      chip.style.opacity=Math.min(1,q*3).toFixed(3); const w=chip.offsetWidth;
      chip.style.transform=`translate(${(lerp(p0.x,540,q)-w/2).toFixed(1)}px,${(lerp(p0.y,600,q)-48).toFixed(1)}px) scale(${(lerp(.8,1.22,q)+pulse(t,T.COPY+.36,.05,12,24)).toFixed(4)}) rotate(${(-4*q).toFixed(2)}deg)`; } else if(t<T.BACK) chip.style.opacity=0;
    CURSOR.draw(t);
  }
  return {frame,camAt,toS,chip,ents};
})();
