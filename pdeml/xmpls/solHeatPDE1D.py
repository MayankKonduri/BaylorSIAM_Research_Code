import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("../")

from HeatPDE import *


n = 128
nt = 10*n

# define RDEPDE object
pde = HeatPDE()
pde.do_setup( n, nt )

u = pde.fwd_sol( 1.0, 20.0 )

x = np.linspace(0, 1, n+1 )

fig, ax = plt.subplots(1)
plt.plot(x, u[:,-1])
plt.show()
