/* Helpers compartidos: reloj puro, curvas, PRNG con semilla. Sin estado acumulado. */
function mulberry(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v)), lerp=(a,b,u)=>a+(b-a)*u;
const seg=(t,a,b)=>clamp((t-a)/(b-a),0,1);
const E={lin:u=>u,inQ:u=>u*u,outQ:u=>1-(1-u)*(1-u),inC:u=>u*u*u,outC:u=>1-Math.pow(1-u,3),
  ioC:u=>u<.5?4*u*u*u:1-Math.pow(-2*u+2,3)/2, outE:u=>u>=1?1:1-Math.pow(2,-10*u),
  outB:u=>{const c=1.9;return 1+(c+1)*Math.pow(u-1,3)+c*Math.pow(u-1,2)},
  ioS:u=>-(Math.cos(Math.PI*u)-1)/2, inE:u=>u<=0?0:Math.pow(2,10*u-10)};
// fotogramas clave: [[t, v, curvaHaciaEstaClave], ...]
function kf(t,k){ if(t<=k[0][0])return k[0][1]; for(let i=1;i<k.length;i++){ if(t<=k[i][0]){const u=(t-k[i-1][0])/(k[i][0]-k[i-1][0]);return lerp(k[i-1][1],k[i][1],(k[i][2]||E.lin)(u));}} return k[k.length-1][1]; }
// pulso amortiguado tras un impacto en h
const pulse=(t,h,amp,decay=11,freq=26)=> t<h?0:amp*Math.exp(-(t-h)*decay)*Math.cos((t-h)*freq);
const $=id=>document.getElementById(id);
const px=v=>v.toFixed(2)+"px";
// velocidad numerica de una funcion escalar (unidades por segundo)
const vel=(f,t)=>(f(t+1/60)-f(t-1/60))*30;
