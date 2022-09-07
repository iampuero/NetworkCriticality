import numpy as np
import matplotlib.pyplot as plt
from anarpy.utils.FCDutil.fcd import phaseFC
import networkx as nx
from numba.experimental import jitclass
from sys import argv



def get_taskId():
    try:
        taskId = int(argv[1])
    except:
        taskId = 0
    return taskId

class Kuramoto():
    def __init__(self,cm,omega0,dt,D=0.01):
        self.omega0 = omega0
        self.cm = cm
        self.N = cm.shape[0]
        self.D = 0.00#np.random.uniform(0.5,1.5,size=N)  #Variance, not SD
        self.sqDt=np.sqrt(2*D/dt)
        
    def iter(self,x,t):
        return self.omega0 + np.sum(self.cm*np.sin(x - x[:,None]),axis=-1)# + self.sqDt*np.random.normal(0,1,self.N)

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
    
    #@njit()
    def simulate(self):
        for i,t in enumerate(range(self.time)):
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
    
    def get_cmat2(self):
        return phaseFC(self.phase)


def lattice1d(N,g=1,n=0):
    cm = nx.to_numpy_array(nx.cycle_graph(N))
    for i in range(n):
        i+=1 
        cm+=np.diag([1]*(N-i),i)+np.diag([1]*(N-i),-i)
    cm = cm*g
    return cm

def plotter():
    pass
 
if __name__== "__main__":
    taskId = get_taskId()
    N = 800
    T = 30
    mu = 0.01
    std = 0.1
    dt = 0.01
    g = np.round(0.01*taskId,3)
    CM = lattice1d(N,g,3)
    Omega0 = np.random.lognormal(mu,std,N)*2*np.pi
    kura = Kuramoto(CM,Omega0,dt)
    sim= Simulator(kura,N,dt,20,T)

    sim.equil()
    xt,phase = sim.simulate()
    #cmat = sim.get_cmat()
    _,r,meta = sim.get_metrics()
    print(g,r,meta)

    if 0:
        #PLOTS
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

        plt.savefig(f"plots/fig2_{taskId}.png")
    
    np.save(f"data/x_{g}",xt)
    np.save(f"tmp/grmeta_{N}_{g}",[g,r,meta])
