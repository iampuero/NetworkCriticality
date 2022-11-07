from os import listdir
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from utils import getArg


N = getArg(1,int)
label = getArg(2,str)

#data = np.genfromtxt("slurm_out/output_484004.out",delimiter=" ")
#Load files
#data = np.vstack([np.load("tmp/"+filename) for filename in listdir("tmp/") if jid in filename])
#data = np.vstack([np.load(f"tmp/grmeta_{label}_{N}_{np.round(0.001*i,3)}.npy") for i in range(1,gnum+1)]) 
data = np.vstack([np.load(f"tmp/grmeta_wico_{N}_{label}_{n}.npy") for n in range(1,150)])
gnum = data.shape[0]

#Save and plot
#np.save(f"data/plot/grmeta_lsp_{N}_{label}",data)
plt.subplot(2,1,1)
plt.suptitle(f"id:{label} N={N} G#{gnum}")
plt.scatter(data[:,0],data[:,1],marker=".")
plt.xlabel("G")
plt.ylabel("r")
plt.xscale("log")
plt.subplot(2,1,2)
plt.scatter(data[:,0],data[:,2],marker=".")
plt.xlabel("G")
plt.ylabel("meta")
plt.xscale("log")
plt.tight_layout()
plt.savefig(f"plots/grmeta_wico_{label}_{N}.png")