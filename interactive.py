import streamlit as st
import matplotlib.pyplot as plt
from anarpy.utils.FCDutil.fcd import phaseFC

from CKuramoto import *

np.random.seed(321)

fixed = st.checkbox("Fixed values (40,50,0,0.1,0.01,0.1)",False)

if fixed:
    N = 40
    T = 50
    mu = 0
    std = 0.1
    dt = 0.01
    g = np.round(0.01*10,3)
else:
    N = st.select_slider("N",[10,30,50,100,200,500])
    T = 50
    mu = 0
    std = 0.1
    dt = 0.01
    g = st.slider("G",0.01,5.0,0.1,0.05)


CM = lattice1d(N,g,3)
Omega0 = np.random.lognormal(mu,std,N)*2*np.pi
kura = Kuramoto(CM,Omega0,dt)
sim= Simulator(kura,N,dt,20,T)

sim.equil()
xt,phase = sim.simulate()
cmat = sim.get_cmat2()
_,r,meta = sim.get_metrics()
print(g,r,meta)


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

st.pyplot(plt.gcf())