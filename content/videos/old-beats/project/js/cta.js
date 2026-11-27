/* Escena 5: palabras al centro de la rueda (misma entrada que wheel v7: pequenas, bajas y ladeadas, y no dejan de crecer) y tarjeta final. */
const CTA=(function(){
  const cw=$("cw"), wt=$("cwt"), end=$("endcard"), l1=$("end-l1"), l2=$("end-l2"), sub=$("end-sub"), brand=$("end-brand");
  const W=[[T.W.COMMENT,"COMMENT"],[T.W.GALER,"GALER",1],[T.W.TO,"TO STORE"],[T.W.ALL,"ALL YOUR"],[T.W.BEAT,"BEAT HISTORY"],[T.W.ONLINE,"ONLINE"]]; let cur=-1;
  function frame(t){
    let i=-1; for(let k=0;k<W.length;k++) if(t>=W[k][0]) i=k;
    if(i<0||t>=T.END){ cw.style.opacity=0; } else { const [a,s,p]=W[i], b=i+1<W.length?W[i+1][0]:T.END;
      if(cur!==i){ cur=i; wt.textContent=s; wt.className="wt"+(p?" pill":""); }
      const u=E.outC(seg(t,a,a+.16)), v=Math.sin(Math.PI/2*seg(t,a+.16,b+.4));
      cw.style.opacity=1; wt.style.transform=`translateY(${(lerp(26,0,u)-30*v).toFixed(2)}px) rotate(${lerp(-3.5,0,u).toFixed(2)}deg) scale(${((p?1.25:1)*(lerp(.85,.95,u)+.06*v)).toFixed(4)})`; }
    if(t<T.END){ end.style.opacity=0; return; }
    end.style.opacity=1; const a=T.END+.07, d=seg(t,T.END,T.END+1.7);
    [l1,l2].forEach((el,k)=>{ const a2=a+k*.1, u=E.outC(seg(t,a2,a2+.12)); el.style.opacity=t>=a2?1:0; el.style.transform=`translateY(${lerp(12,0,u).toFixed(2)}px) scale(${(lerp(.86,.93,u)+.09*(1-Math.pow(1-seg(t,a2+.12,a2+2.1),2))).toFixed(4)}) rotate(${k?lerp(-5,-2,u).toFixed(2):0}deg)`; });
    sub.style.opacity=seg(t,a+.2,a+.3).toFixed(3); sub.style.transform=`translateY(${(-14*d).toFixed(2)}px)`; brand.style.transform=`scale(${(1+.03*Math.sin(Math.PI/2*d)).toFixed(4)})`;
  }
  return {frame};
})();
