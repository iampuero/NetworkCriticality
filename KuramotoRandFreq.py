# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:17:34 2019

@author: Patricio Orio
"""

import numpy as np
import matplotlib.pyplot as plt

def Kur(X,t):
    return Omega0 + np.sum(CM*np.sin(X - X[:,None]),axis=-1) + sqDt*np.random.normal(0,1,N)

def ConMatrix(N,p=0.3,cmin=-0.5,cmax=0.5):
    CM=np.random.uniform(cmin,cmax,size=(N,N))
    Mask=np.random.binomial(1,p,size=(N,N))
    CM*=Mask
    CM[np.triu_indices_from(CM)]=0
    CM = CM+CM.T
    CM[np.diag_indices(N)]=0
    return CM

tstop=100
dt=0.01
time=np.arange(0,tstop,dt)

t_equil=20
t0=int(t_equil/dt)

N=80
mu = 0.5
std = 1.5
Omega0=np.random.lognormal(mu,std,N)*2*np.pi
#mu=np.zeros(N)#10.*np.arange(N)
D=0.01#np.random.uniform(0.5,1.5,size=N)  #Variance, not SD
sqDt=np.sqrt(2*D/dt)

CM=ConMatrix(N,p=1,cmin=0.0,cmax=0.1)

X_t=np.zeros((len(time),N))
X=np.zeros(N) #np.zeros(N)


for i in range(t0):
    X += dt*Kur(X,0)

for i,t in enumerate(time):
    X_t[i]=X
    X += dt*Kur(X,t)

# X_t=X_t[::10,:]
# time=time[::10]
phase=X_t%(2*np.pi)

phasesync = np.abs(np.mean(np.exp(1j*phase),axis=1))
R = np.mean(phasesync)
meta = np.var(phasesync)

#%%

#CMat=np.cov(X_t,rowvar=False)

# REEMPLAZAR CON anarpy.utils.FCDutil.fcd.phaseFC
CMat=np.mean(np.abs((np.exp(1j*phase[:,None,:])+np.exp(1j*phase[:,:,None]))/2),0)
    
plt.figure(1)
plt.clf()
plt.subplot(311)
plt.plot(time,X_t+8*np.arange(N))
plt.xlim(0,10)
# plt.legend(["%d"%i for i in range(N)])

plt.subplot(312)
plt.plot(time, np.sin(phase))
plt.xlim(0,10)
plt.subplot(325)
#Cmax=np.max(abs(CMat))
plt.imshow(CMat,cmap='jet',vmin=0,vmax=1)
plt.title('static FC')
plt.colorbar()

plt.subplot(326)
#Cmax=np.max(abs(CM))
plt.imshow(CM,cmap='jet',vmin=0,vmax=1)
plt.title('CM')
plt.colorbar()

plt.savefig("plots/fig.png")
np.save("archivo",X_t)
