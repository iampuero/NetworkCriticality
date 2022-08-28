import matplotlib.pyplot as plt
import numpy as np


A=np.random.random((10,2))
plt.scatter(A[:,0],A[:,1])
plt.savefig("plots/scatter.png")