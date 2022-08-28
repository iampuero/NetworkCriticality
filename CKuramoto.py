import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Kuramoto():
    def __init__(self,cm,omega0,dt,D=0.01):
        self.omega0 = omega0
        self.cm = cm
        self.N = cm.shape[0]
        self.D = 0.01#np.random.uniform(0.5,1.5,size=N)  #Variance, not SD
        self.sqDt=np.sqrt(2*D/dt)
        
    def iter(self,x):
        return self.omega0 + np.sum(self.cm*np.sin(x - x[:,None]),axis=-1) + self.sqDt*np.random.normal(0,1,self.N)

class Simulator():
    def __init__(self,model,N,dt,t_stop,t_equil):
        self.model = model
        self.dt = dt
        self.t_equil = t_equil
        self.t_stop = t_stop
        self.t0 = int(t_equil/dt)
        self.time = int(t_stop/dt)
        self.x_t = np.zeros((self.time,N))
        self.x = np.zeros(N)
        self.phase = None
    
    def equil(self):
        for i in range(self.t0):
            self.x += self.dt*self.model.iter(self.x,0)
    
    def simulate(self,time):
        for i,t in enumerate(range(time)):
            self.x_t[i]=self.x
            self.x += self.dt*self.model.iter(self.x,t)
        self.phase = self.x_t%(2*np.pi)
        return self.x_t,self.phase
    
    def get_metrics(self):
        phasesync = np.abs(np.mean(np.exp(1j*self.phase),axis=1))
        r = np.mean(phasesync)
        meta = np.var(phasesync)
        return phasesync,r,meta
    
    def get_cmat(self):
        return np.mean(np.abs((np.exp(1j*self.phase[:,None,:])+np.exp(1j*self.phase[:,:,None]))/2),0)


def plotter():
    pass

if __name__== "main":
    N = 20
    mu = 0.5
    std = 1.5
    dt = 0.01
    CM = nx.to_numpy_array(nx.cycle_graph(N))
    Omega0 = np.random.lognormal(mu,std,N)*2*np.pi
    kura = Kuramoto(CM,Omega0,dt)
    sim= Simulator(kura,N,dt,20,100)

    sim.equil()
    xt,phase = sim.simulate()
    cmat = sim.get_cmat()

    #PLOTS
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