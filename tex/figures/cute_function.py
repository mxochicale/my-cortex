"""Plot the function sin(1 / XY)."""

import matplotlib.pyplot as plt
import numpy as np

# Compute sin(x)+sin(y)
sz = 5000
X = np.linspace(-50, 50, sz)
Y = np.linspace(-50, 50, sz)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X) + np.sin(Y)

# Plot it
fig, ax = plt.subplots(1)
im = ax.imshow(Z, cmap=plt.get_cmap("plasma"),
               origin="lower")
		#, extent=(-1, 1, -1, 1))
plt.colorbar(im, shrink=1, aspect=10)
ax.set_xlabel("X", fontsize=16)
ax.set_ylabel("Y", fontsize=16)

# Save it
fig.savefig("cute_function.pdf", bbox_inches="tight")
