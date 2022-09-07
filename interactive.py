import streamlit as st
import matplotlib.pyplot as plt
from time import time

from CKuramoto import *

np.random.seed(321)

fixed = st.checkbox("Fixed values (40,50,0,0.1,0.01,0.1)",False)

st.sidebar.write("**Params**")

if fixed:
    N = 40
    T = 50
    mu = 0
    std = 0.1
    dt = 0.01
    g = np.round(0.01*10,3)
else:
    N = st.sidebar.select_slider("N",[10,30,50,100,200,500])
    T = st.sidebar.select_slider("T",[10,20,30,50])
    mu = st.sidebar.select_slider("mu",[0,0.01,0.05])
    std = st.sidebar.select_slider("std",[0.01,0.05,0.1])
    dt = 0.01
    g = st.sidebar.slider("G",0.01,5.0,0.1,0.05)


CM = lattice1d(N,g,3)
Omega0 = np.random.lognormal(mu,std,N)*2*np.pi
kura = Kuramoto(CM,Omega0,dt)
sim= Simulator(kura,N,dt,20,T)

start = time()

sim.equil()
xt,phase = sim.simulate()
timesim = time()

cmat = sim.get_cmat2()
timecmat = time()

_,r,meta = sim.get_metrics()
timemetrics = time()

st.write(f"g = {g}  r = {r}  meta = {meta}")


plt.figure(1)
plt.clf()
plt.subplot(311)
plt.plot(np.arange(0,20,dt),xt+8*np.arange(N))
plt.xlim(0,10)
# plt.legend(["%d"%i for i in range(N)])

plt.subplot(312)
plt.plot(np.arange(0,20,dt), np.sin(phase))
plt.xlim(0,10)
plt.subplot(325)
#Cmax=np.max(abs(CMat))
plt.imshow(cmat,cmap='jet',vmin=0,vmax=1)
plt.title('static FC')
plt.colorbar()

plt.subplot(326)
#Cmax=np.max(abs(CM))
plt.imshow(CM,cmap='jet',vmin=0,vmax=1)
plt.title('CM')
plt.colorbar()
plt.tight_layout()

st.pyplot(plt.gcf())

timeplots = time()

st.sidebar.write("**Times**")
st.sidebar.write(f"Simulation: {np.round(timesim-start,3)}[s]")
st.sidebar.write(f"Cmat: {np.round(timecmat-timesim,3)}[s]")
st.sidebar.write(f"Metrics: {np.round(timemetrics-timecmat,3)}[s]")
st.sidebar.write(f"Plots: {np.round(timeplots-timemetrics,3)}[s]")