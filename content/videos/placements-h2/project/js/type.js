/* Tipografia cinetica reutilizable: palabras sueltas en mayusculas que se ajustan a un ancho.
   const w = KW("ASAP", 840);  w.put(x, y, {s, o, by, r})  -> centro en (x,y), escala, opacidad, desenfoque vertical, giro */
const KT={list:[],ready:false};
function KW(text,fit,opt={}){
  const el=document.createElement("div"); el.className="kw"+(opt.ink?" ink":""); el.textContent=text;
  (opt.parent||$("kt")).appendChild(el);
  const o={el,text,fit,fs:100,w:fit,h:86,opt,
    measure(){ el.style.fontSize="100px"; const w100=el.offsetWidth||fit; this.fs=opt.like?opt.like.fs:Math.min(opt.max||999,100*fit/w100); el.style.fontSize=this.fs.toFixed(2)+"px"; this.w=w100*this.fs/100; this.h=this.fs*.86; },
    put(x,y,p={}){ const s=p.s==null?1:p.s, op=p.o==null?1:p.o; if(op<=.001){ if(this._on!==0){el.style.opacity=0;this._on=0;} return; } this._on=1;
      el.style.opacity=op.toFixed(3);
      el.style.transform=`translate3d(${(x-this.w/2).toFixed(2)}px,${(y-this.h/2).toFixed(2)}px,0) rotate(${(p.r||0).toFixed(2)}deg) scale(${(s*(p.sx||1)).toFixed(4)},${(s*(p.sy||1)).toFixed(4)})`;
      const b=p.b||0, by=p.by||0; el.style.filter=(b>.3||by>.6)?`blur(${Math.max(b,by*.35).toFixed(1)}px)`:"none"; }
  };
  o.measure(); KT.list.push(o); return o;
}
function ktCheck(){ if(KT.ready)return; if(document.fonts&&document.fonts.check('900 100px "BG Display"')){ KT.list.forEach(o=>o.measure()); KT.ready=true; } }
if(document.fonts){ document.fonts.load('900 100px "BG Display"'); ["400","500","600","700"].forEach(w=>document.fonts.load(w+' 30px "BG UI"')); }
// entrada tipo golpe: llega grande y rapida, asienta con un rebote corto
const slam=(t,t0,d=.13)=>{const u=seg(t,t0,t0+d); return {o:t>=t0?1:0, s:t<t0?1:lerp(1.55,1,E.outC(u))+pulse(t,t0+d,.035,14,30), b:(1-u)*10};};
