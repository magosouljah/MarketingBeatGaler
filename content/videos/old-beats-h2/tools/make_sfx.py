#!/usr/bin/env python3
"""Sonido de arranque propio: dos notas sueltas I -> V con pluck de onda senoidal y un poco de reverb (sin acordes)."""
import wave
from pathlib import Path
import numpy as np
SR=48000; OUT=Path(__file__).resolve().parent.parent/"project/assets/sfx/startup.wav"
def pluck(f,d=.9):
    t=np.arange(int(SR*d))/SR
    return (np.sin(2*np.pi*f*t)+.18*np.sin(4*np.pi*f*t)*np.exp(-t*14))*np.exp(-t*7.5)*np.minimum(1,t/.004)
x=np.zeros(int(SR*1.9)); a=pluck(523.25); b=pluck(783.99)          # C5 -> G5
x[:len(a)]+=a*.8; o=int(.20*SR); x[o:o+len(b)]+=b*.9
rng=np.random.default_rng(7); n=int(SR*1.1); ir=rng.standard_normal((2,n))*np.exp(-np.arange(n)/SR*5.5)[None,:]; ir[:,:int(.012*SR)]=0
wet=np.stack([np.convolve(x,ir[c])[:len(x)] for c in (0,1)]); wet/=np.abs(wet).max()
y=np.stack([x,x])*.8+wet*.22; y/=np.abs(y).max()/.7; y[:,-2400:]*=np.linspace(1,0,2400)
w=wave.open(str(OUT),"wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((y.T*32767).astype("<i2").tobytes()); w.close(); print("OK",OUT)
