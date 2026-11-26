#!/usr/bin/env python3
"""Sintetiza los whooshes del proyecto (ruido con banda que barre + cola de aire, estereo).
   python tools/make_sfx.py   ->  project/assets/sfx/whoosh_a.wav, whoosh_b.wav
Sustituyen a whoosh1/whoosh2 heredados de add-finder (mono, cortados en seco)."""
import numpy as np, librosa, soundfile as sf
from pathlib import Path
SR=48000; OUT=Path(__file__).resolve().parent.parent/"project/assets/sfx"
def whoosh(dur, f0, f1, f2, peak_at, seed, width=1.1):
    rng=np.random.default_rng(seed); n=int(dur*SR); out=[]
    for ch in range(2):
        x=rng.standard_normal(n+4096)
        S=librosa.stft(x,n_fft=2048,hop_length=256); f=librosa.fft_frequencies(sr=SR,n_fft=2048)[:,None]+1
        t=np.linspace(0,1,S.shape[1])[None,:]
        # centro de la banda: sube hasta el pico y cae; anchura en octavas
        u=np.where(t<peak_at,t/peak_at,(t-peak_at)/(1-peak_at))
        fc=np.where(t<peak_at,f0*(f1/f0)**(u**1.6),f1*(f2/f1)**(u**.7))
        band=np.exp(-0.5*(np.log2(f/fc)/width)**2)+0.10*np.exp(-0.5*(np.log2(f/(fc*3.2))/.9)**2)
        y=librosa.istft(S*band,hop_length=256,length=n+4096)[2048:2048+n]
        out.append(y)
    y=np.stack(out,1); tt=np.linspace(0,1,n)
    env=np.where(tt<peak_at,(tt/peak_at)**2.6,np.exp(-(tt-peak_at)/(1-peak_at)*5.0))
    env*=np.minimum(1,(1-tt)/.08)                       # sin corte en seco al final
    pan=0.5+0.38*np.sin((tt-peak_at)*2.2)               # cruza de un lado al otro
    y[:,0]*=env*np.sqrt(1-pan); y[:,1]*=env*np.sqrt(pan)
    return (y/np.abs(y).max()*0.7).astype(np.float32)
OUT.mkdir(parents=True,exist_ok=True)
sf.write(OUT/"whoosh_a.wav",whoosh(0.62,180,2600,500,0.56,11),SR,subtype="PCM_24")   # transicion de escena
sf.write(OUT/"whoosh_b.wav",whoosh(0.46,260,3600,900,0.50,23,width=.9),SR,subtype="PCM_24")  # salida corta
print("ok",OUT)
