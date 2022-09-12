import streamlit as st
import matplotlib.pyplot as plt
from time import time

from CKuramoto import *

np.random.seed(111)

computecmat = st.checkbox("Compute FC",False)
st.sidebar.write("**Params**")


N = st.sidebar.select_slider("N",[10,30,50,100,200,500])
T = st.sidebar.select_slider("T",[10,20,30,50])
mu = st.sidebar.select_slider("mu",[0,0.01,0.05])
std = st.sidebar.select_slider("std",[0.01,0.05,0.1])
dt = 0.01


st.sidebar.write("**CM Params**")
cmtype = st.sidebar.selectbox("Type:",["Lattice1D","Random"])
g = st.sidebar.number_input("G",0.01,10.0,0.1)
if cmtype=="Lattice1D":
    st.sidebar.write("_Lattice CM Params_")
    neig = st.sidebar.slider("Neighbors",0,min(N,10),0,1)
    CM = lattice1d(N,g,neig)
else:
    st.sidebar.write("_Random CM Params_")
    prob = st.sidebar.slider("Probability",0.01,0.3,0.08,0.01)
    CM = randomCM(N,prob,g)

cmat = np.zeros((N,N))
Omega0 = np.random.lognormal(mu,std,N)*2*np.pi
kura = Kuramoto(CM,Omega0,dt)
sim= Simulator(kura,N,dt,20,T)

start = time()

sim.equil()
xt,phase = sim.simulate()
timesim = time()

if computecmat:
    cmat = sim.get_cmat2()
timecmat = time()

_,r,meta = sim.get_metrics()
timemetrics = time()

st.write(f"**g** = {g}  **r** = {np.round(r,4)}  **meta** = {np.round(meta,5)}")


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



sidexpander = st.sidebar.expander("Exec Times")
sidexpander.write(f"Simulation: {np.round(timesim-start,3)}[s]")
sidexpander.write(f"Cmat: {np.round(timecmat-timesim,3)}[s]")
sidexpander.write(f"Metrics: {np.round(timemetrics-timecmat,3)}[s]")
sidexpander.write(f"Plots: {np.round(timeplots-timemetrics,3)}[s]")
sidexpander.write(f"**Total**: {np.round(timeplots-start,3)}[s]")