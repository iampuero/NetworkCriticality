from webbrowser import get
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from utils import getJobid


jid = getJobid()
N = int(argv[1])
gnum = int(argv[2])
label = argv[3]

#data = np.genfromtxt("slurm_out/output_484004.out",delimiter=" ")
#Load files
data = np.vstack([np.load(f"tmp/grmeta_{jid}-{i}.npy") for i in range(1,gnum+1)])

#Save and plot
np.save(f"data/plotdata/grmeta_{label}_{N}_{gnum}",data)
plt.subplot(2,1,1)
plt.suptitle(f"id:{label} N={N} G#{gnum}")
plt.scatter(data[:,0],data[:,1],marker=".")
plt.xlabel("G")
plt.ylabel("r")
plt.subplot(2,1,2)
plt.scatter(data[:,0],data[:,2],marker=".")
plt.xlabel("G")
plt.ylabel("meta")
plt.tight_layout()
plt.savefig(f"plots/plot_rmeta_{label}_{N}-{gnum}.png")