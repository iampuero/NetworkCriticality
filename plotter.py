import matplotlib.pyplot as plt
import numpy as np


#data = np.genfromtxt("slurm_out/output_484004.out",delimiter=" ")
data = np.vstack([np.load(f"tmp/grmeta_{np.round(0.01*i,3)}.npy") for i in range(1,101)]) 

plt.subplot(2,1,1)
plt.scatter(data[:,0],data[:,1])
plt.xlabel("G")
plt.ylabel("r")
plt.subplot(2,1,2)
plt.scatter(data[:,0],data[:,2])
plt.xlabel("G")
plt.ylabel("meta")
plt.tight_layout()
plt.savefig("plot_tmp.png")