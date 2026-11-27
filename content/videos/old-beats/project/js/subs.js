/* Subtitulos sobre el video de FL: bloques cortos en mayusculas, cada uno entra con su palabra. */
const SUBS=(function(){ const el=$("sub"), sp=$("subt"); let cur=-1;
  function frame(t){ let i=-1; for(let k=0;k<T.SUBS.length;k++){ const [a,,b]=T.SUBS[k]; if(t>=a&&t<b)i=k; }
    if(i<0||t<T.OLD-.05||t>=T.D){ el.style.opacity=0; return; }
    const [a,s]=T.SUBS[i], a2=Math.max(a,T.OLD-.05), u=E.outC(seg(t,a2,a2+.1)); if(cur!==i){ cur=i; sp.textContent=s; }
    el.style.opacity=1; sp.style.transform=`translateY(${lerp(18,0,u).toFixed(1)}px) scale(${lerp(.9,1,u).toFixed(4)})`; }
  return {frame}; })();
