/* Chat (Story + DM): se construye una vez y sirve a la escena 1 (hook) y a la escena 4 (cierre).
   Conversacion ficticia e ilustrativa. Coordenadas internas = tarjeta de 860x1470. */
const IGS={ artist:"noirvelle", cov:["031","023","034"] };
const IG=(function(){
  const root=$("sIG");
  const ic={
    back:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 4l-8 8 8 8"/></svg>`,
    phone:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>`,
    video:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="6" width="13" height="12" rx="3"/><path d="M15.5 10.5l6-3.5v10l-6-3.5z"/></svg>`,
    heart:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.5s-8-4.9-8-10.6A4.4 4.4 0 0 1 12 7.4a4.4 4.4 0 0 1 8 2.5c0 5.7-8 10.6-8 10.6z"/></svg>`,
    plane:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M21 3L10 14M21 3l-7 18-4-7-7-4z"/></svg>`,
    x:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.1" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg>`,
    dots:`<svg viewBox="0 0 24 24" fill="#fff"><circle cx="5" cy="12" r="1.9"/><circle cx="12" cy="12" r="1.9"/><circle cx="19" cy="12" r="1.9"/></svg>`,
    cam:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8.5A2.5 2.5 0 0 1 5.5 6H8l1.5-2h5L16 6h2.5A2.5 2.5 0 0 1 21 8.5v9a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 17.5z"/><circle cx="12" cy="13" r="3.6"/></svg>`,
    mic:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11.5a6.5 6.5 0 0 0 13 0M12 18v3"/></svg>`,
    img:`<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.6"/><path d="M21 15l-5-5L5 21"/></svg>`
  };
  const av=(sz,plain)=>`<div class="avatar${plain?" plain":""}" style="width:${sz}px;height:${sz}px"><i></i></div>`;
  root.innerHTML=`<div id="igcam"><div id="phone">
    <div id="dm">
      <div id="dm-thread">
        <div class="dm-ts" id="dm-ts" style="top:158px">Today 4:17 PM</div>
        <div class="dm-cap" id="dm-cap" style="top:212px">You replied to their story</div>
        <div id="dm-thumb"></div>
        <div class="bub me" id="b-me" style="top:524px">what u need?</div>
        <div class="dm-av" id="a-them" style="top:676px">${av(48,true)}</div>
        <div id="dm-dots" style="top:644px"><i style="left:30px"></i><i style="left:54px"></i><i style="left:78px"></i></div>
        <div class="bub them" id="b-them" style="top:644px">send me some dark rnb <b>ASAP</b></div>
        <div id="dm-link" style="top:764px"><div class="art">
            <img src="assets/covers/cover-${IGS.cov[0]}.jpg" style="left:44px;transform:rotate(-7deg)" alt="">
            <img src="assets/covers/cover-${IGS.cov[2]}.jpg" style="left:294px;transform:rotate(7deg)" alt="">
            <img src="assets/covers/cover-${IGS.cov[1]}.jpg" style="left:169px;top:28px;width:194px;height:194px" alt=""></div>
          <div class="inf"><div class="t1">dark rnb pack</div><div class="t2">3 beats · BeatGaler</div><div class="url">beatgaler.com/p/dark-rnb</div></div></div>
        <div id="dm-seen">Seen</div>
        <div class="dm-av" id="a-them2">${av(48,true)}</div>
        <div id="dm-dots2" class="dots2"></div>
        <div class="bub them" id="b-fire"><b>FIRE</b> 🔥</div>
      </div>
      <div id="dm-head"><div class="back">${ic.back}</div><div class="av">${av(68)}</div><div class="nm">${IGS.artist}</div><div class="st">Active now</div>
        <div class="ic" style="left:716px">${ic.phone}</div><div class="ic" style="left:788px">${ic.video}</div></div>
      <div id="dm-in"><div class="cam">${ic.cam}</div><div class="ph">Message…</div><div class="txt">beatgaler.com/p/dark-rnb</div>
        <div class="ic" id="in-mic" style="left:694px">${ic.mic}</div><div class="ic" id="in-img" style="left:756px">${ic.img}</div><div class="send">Send</div></div>
    </div>
    <div id="story">
      <div id="st-bg"></div>
      <div id="st-shade"></div>
      <div id="st-stick"><span>Send beats</span></div>
      <div id="st-ui"><div id="st-bar"><i></i></div><div class="av">${av(68)}</div><div class="nm">${IGS.artist}<span>2h</span></div>
        <div class="ic" style="left:724px">${ic.dots}</div><div class="ic" style="left:790px">${ic.x}</div>
        <div id="st-reply"><div class="ph">Send message</div><div class="txt"></div></div>
        <div class="heart">${ic.heart}</div><div class="plane">${ic.plane}</div><div id="st-send">Send</div></div>
    </div>
  </div></div>`;
  const cam=$("igcam"), phone=$("phone"), story=$("story"), stui=$("st-ui"), stbar=$("st-bar").firstChild, stick=$("st-stick"), stbg=$("st-bg");
  const rph=root.querySelector("#st-reply .ph"), rtxt=root.querySelector("#st-reply .txt"), stsend=$("st-send"), heart=root.querySelector(".heart"), plane=root.querySelector(".plane"), reply=$("st-reply");
  const head=$("dm-head"), inp=$("dm-in"), thread=$("dm-thread"), ts=$("dm-ts"), cap=$("dm-cap"), bme=$("b-me"), bthem=$("b-them"), athem=$("a-them"), dots=$("dm-dots"), dotI=[...dots.children];
  const link=$("dm-link"), seen=$("dm-seen"), bfire=$("b-fire"), athem2=$("a-them2"), inPh=inp.querySelector(".ph"), inTxt=inp.querySelector(".txt"), inSend=inp.querySelector(".send"), inMic=$("in-mic"), inImg=$("in-img");
  const TYPED="what u need?", PH={x:110,y:130};
  // posiciones del cierre dentro del hilo
  const LINKTOP=764, FIRETOP=1196;
  seen.style.top="1160px"; athem2.style.top=(FIRETOP+32)+"px"; bfire.style.top=FIRETOP+"px";
  const dots2=$("dm-dots2"); dots2.id="dm-dots2"; dots2.style.cssText=`position:absolute;left:88px;top:${FIRETOP}px;width:126px;height:80px;border-radius:40px;background:#262626;transform-origin:0 100%;opacity:0`;
  dots2.innerHTML=`<i style="position:absolute;top:31px;left:30px;width:18px;height:18px;border-radius:50%;background:#9a9a9a"></i><i style="position:absolute;top:31px;left:54px;width:18px;height:18px;border-radius:50%;background:#9a9a9a"></i><i style="position:absolute;top:31px;left:78px;width:18px;height:18px;border-radius:50%;background:#9a9a9a"></i>`;
  const dot2I=[...dots2.children];

  // tipografia
  const ASAP=[KW("ASAP",800)], F1=KW("FIRST",560), FIRST=[F1,KW("TO",600,{like:F1}),KW("SEND",600,{like:F1}),KW("YOURS",600,{like:F1})];
  const OPP=KW("OPPORTUNITY",840), IM=KW("I’M",330), READY=KW("READY",840);
  const fe0=$("vb0fe");

  // camara: punto de la capa (fx,fy) -> punto de pantalla (sx,sy), escala y giros
  function setCam(c){ cam.style.transform=`translate3d(${c.sx.toFixed(2)}px,${c.sy.toFixed(2)}px,${(c.z||0).toFixed(1)}px) rotateY(${(c.ry||0).toFixed(2)}deg) rotateX(${(c.rx||0).toFixed(2)}deg) rotateZ(${(c.rz||0).toFixed(2)}deg) scale(${c.s.toFixed(4)}) translate(${(-c.fx).toFixed(2)}px,${(-c.fy).toFixed(2)}px)`;
    cam.style.filter=(c.blur||0)>.3?`blur(${c.blur.toFixed(1)}px)`:"none"; cam.style.opacity=c.o==null?1:c.o.toFixed(3); }
  const toScreen=(c,x,y)=>({x:c.sx+(PH.x+x-c.fx)*c.s, y:c.sy+(PH.y+y-c.fy)*c.s});
  const H=HOOK;
  function cam1(t){
    const fx=kf(t,[[0,540],[H.SEND,540],[H.SEND+.4,430,E.ioC],[H.MSG-.02,400,E.lin],[H.MSG+.22,450,E.outC],[9,450]]);
    const fy=kf(t,[[0,865],[.24,865],[.8,1260,E.ioC],[H.SEND,1275,E.lin],[H.SEND+.4,812,E.ioC],[H.MSG,812],[H.MSG+.22,800,E.outC],[9,800]]);
    // tras enviar: directo a los tres puntitos y empuje lento mientras escribe (expectativa); al llegar el mensaje abre para leerlo
    let s=kf(t,[[0,1.09],[.24,1,E.outC],[.8,1.24,E.ioC],[H.SEND,1.27,E.lin],[H.SEND+.4,1.45,E.ioC],[H.MSG-.02,1.78,E.inQ],[H.MSG+.22,1.6,E.outC],[H.PULL,1.68,E.lin],[H.FIRST,.52,E.ioC],[H.WHIP,.47,E.lin],[9,.47]]);
    const sx=kf(t,[[0,540],[H.SEND,540],[H.SEND+.4,540,E.ioC],[H.MSG-.02,540],[H.MSG+.22,540,E.outC],[H.PULL,540],[H.FIRST,420,E.ioC],[H.WHIP,396,E.lin],[9,396]]);
    let sy=kf(t,[[0,865],[.24,865],[.8,1010,E.ioC],[H.SEND,1004,E.lin],[H.SEND+.4,800,E.ioC],[H.MSG-.02,800],[H.MSG+.22,760,E.outC],[H.PULL,748,E.lin],[H.FIRST,430,E.ioC],[H.WHIP,404,E.lin],[9,404]]);
    const ry=kf(t,[[0,0],[H.PULL,0],[H.FIRST,22,E.ioC],[H.WHIP,27,E.lin],[9,27]]), rx=kf(t,[[0,0],[H.PULL,0],[H.FIRST,8,E.ioC],[9,8]]), rz=kf(t,[[0,0],[H.PULL,0],[H.FIRST,-6,E.ioC],[H.WHIP,-7.5,E.lin],[9,-7.5]]);
    s*=1+pulse(t,.46,.018,12,24)+pulse(t,H.SEND,-.02,12,24)+pulse(t,1.66,.012,12,24)+pulse(t,H.MSG,.022,11,24);
    const wu=E.inC(seg(t,H.WHIP,H.WHIP+.26)); sy-=wu*2300;
    return {fx,fy,s,sx,sy,ry,rx,rz,blur:2.5*seg(t,H.PULL+.2,H.FIRST)+wu*10,o:1};
  }
  function common(t){ // estado del hilo comun a las dos escenas
    stbg.style.transform=`scale(${(1.02+Math.min(t,6)*.012).toFixed(4)}) translate(${(Math.sin(t*.8)*6).toFixed(1)}px,${(-Math.min(t,6)*5).toFixed(1)}px)`;
  }
  function s1(t){
    const c=cam1(t); setCam(c); common(t);
    // Story
    stbar.style.transform=`scaleX(${(.31+t/7).toFixed(4)})`;
    const sp=E.outB(seg(t,0,.26)); stick.style.transform=`rotate(-3deg) scale(${(.72+.28*sp+pulse(t,.46,.03,12,26)).toFixed(4)})`;
    const n=Math.round(TYPED.length*seg(t,H.TYPE0,H.TYPE1)), typing=t>=H.TYPE0-.12;
    rph.style.opacity=typing?0:1;
    const caret=(t<H.TYPE1)||Math.floor(t*3)%2===0;
    rtxt.innerHTML=typing?TYPED.slice(0,n).replace(/ /g,"&nbsp;")+`<i class="car" style="opacity:${caret?1:0}"></i>`:"";
    reply.style.borderColor=typing?"#fff":"rgba(255,255,255,.72)";
    const sa=E.outC(seg(t,H.TYPE0+.02,H.TYPE0+.2)); stsend.style.opacity=sa.toFixed(3);
    stsend.style.transform=`scale(${((.8+.2*sa)*kf(t,[[0,1],[H.SEND-.1,1],[H.SEND,.88,E.outC],[H.SEND+.12,1,E.outC],[9,1]])).toFixed(4)})`;
    heart.style.opacity=plane.style.opacity=(1-sa).toFixed(3);
    // Story -> miniatura dentro del DM
    const u=E.ioC(seg(t,H.SEND+.02,H.MORPH)), sc=lerp(1,150/860,u);
    story.style.transform=`translate(${(686*u).toFixed(2)}px,${(250*u).toFixed(2)}px) scale(${sc.toFixed(5)})`;
    story.style.borderRadius=(lerp(0,24,u)/sc).toFixed(1)+"px";
    story.style.height=lerp(1470,256/(150/860),u).toFixed(1)+"px";
    stui.style.opacity=(1-seg(u,0,.25)).toFixed(3);
    // DM
    const a=E.outC(seg(t,H.SEND+.06,H.SEND+.32));
    head.style.transform=`translateY(${((a-1)*124).toFixed(1)}px)`; inp.style.transform=`translateY(${((1-a)*150).toFixed(1)}px)`;
    ts.style.opacity=cap.style.opacity=a.toFixed(3); thread.style.transform="none"; story.style.marginTop="0px";
    const bw=bme.offsetWidth, dx=(60)-(860-24-bw), dy=1354-524;
    bme.style.opacity=seg(t,H.SEND,H.SEND+.05).toFixed(3);
    bme.style.transform=`translate(${(dx*(1-u)).toFixed(2)}px,${(dy*(1-u)).toFixed(2)}px) scale(${(1+pulse(t,H.MORPH,.05,14,26)).toFixed(4)})`;
    bme.style.background=u<.35?"rgba(255,255,255,0)":""; 
    const da=seg(t,H.DOTS,H.DOTS+.12)*(1-seg(t,H.MSG-.03,H.MSG));
    dots.style.opacity=da>0?1:0; dots.style.transform=`scale(${(da<=0?.4:(.4+.6*E.outB(Math.min(1,da)))*(1+pulse(t,1.66,.08,10,22))).toFixed(3)})`;
    dotI.forEach((d,k)=>{d.style.transform=`translateY(${(-7*Math.max(0,Math.sin((t-H.DOTS)*16-k*.9))).toFixed(1)}px)`;});
    athem.style.opacity=seg(t,H.DOTS,H.DOTS+.1).toFixed(3);
    const ma=seg(t,H.MSG,H.MSG+.2); bthem.style.opacity=t>=H.MSG?1:0; bthem.style.transform=`scale(${(ma<=0?.5:.5+.5*E.outB(ma)).toFixed(4)})`;
    link.style.opacity=seen.style.opacity=bfire.style.opacity=athem2.style.opacity=dots2.style.opacity=0; inTxt.style.opacity=0; inSend.style.opacity=0; inPh.style.opacity=1; inMic.style.opacity=inImg.style.opacity=1;
    // toque en Send
    const tp=toScreen(c,760,1394), tu=seg(t,H.SEND,H.SEND+.3), tap=$("tap");
    if(t>=H.SEND-.1&&tu<1){ tap.style.opacity=(t<H.SEND?.5*seg(t,H.SEND-.1,H.SEND):.5*(1-tu)).toFixed(3); tap.style.background="rgba(255,255,255,.55)"; tap.style.border="none";
      tap.style.transform=`translate(${tp.x.toFixed(1)}px,${tp.y.toFixed(1)}px) scale(${(t<H.SEND?.5:.5+1.3*E.outC(tu)).toFixed(3)})`; } else if(t<H.DUR) tap.style.opacity=0;
    // ASAP sale del propio mensaje: nace sobre la palabra del globo y crece hasta llenar el ancho
    { const w=ASAP[0], bb=bthem.querySelector("b"), p0=toScreen(c,88+bb.offsetLeft+bb.offsetWidth/2,644+40), s0=bb.offsetHeight*c.s/w.h*.8;
      const g=seg(t,H.ASAP,H.ASAP+.24), q=g<=0?0:E.outB(g), out=E.inC(seg(t,H.PULL-.02,H.PULL+.22));
      w.put(lerp(p0.x,540,q)+out*-200,lerp(p0.y,1150,q)+out*1300,{o:(t>=H.ASAP&&out<1)?1:0,s:lerp(s0,1,q)*(1+(t-H.ASAP)*.035),r:lerp(-10,-3,q),b:(1-seg(g,0,.7))*6+out*14});
      bb.style.display="inline-block"; bb.style.transform=`scale(${(1+pulse(t,H.ASAP,.25,10,22)).toFixed(4)})`; }
    // FIRST / TO / SEND: una palabra por golpe de voz, apiladas abajo a la izquierda; salen hacia arriba como transicion
    const tin=[H.FIRST,H.TO,H.SENDW,H.YOURS], wu2=E.inC(seg(t,H.WHIP,H.WHIP+.3));
    FIRST.forEach((w,k)=>{ const sl=slam(t,tin[k],.12); w.put(120+w.w/2,850+k*w.h*1.03-wu2*2600*(1+.1*k)-(t-H.FIRST)*10,{o:sl.o,s:sl.s,by:wu2>0?60*wu2+10:sl.b}); });
    OPP.put(0,0,{o:0}); IM.put(0,0,{o:0}); READY.put(0,0,{o:0});
  }
  function frame(t){
    const on1=t<H.DUR+.05, on4=t>S.BACK-.02;
    root.style.visibility=(on1||on4)?"visible":"hidden";
    if(on1) s1(t); else if(on4&&IG.s4) IG.s4(t); else { [...ASAP,...FIRST,OPP,IM,READY].forEach(w=>w.put(0,0,{o:0})); }
  }
  return {frame,setCam,toScreen,common,el:{cam,phone,story,stui,head,inp,thread,ts,cap,bme,bthem,athem,dots,link,seen,bfire,athem2,dots2,dot2I,inPh,inTxt,inSend,inMic,inImg},kw:{ASAP,FIRST,OPP,IM,READY},LINKTOP,FIRETOP};
})();
