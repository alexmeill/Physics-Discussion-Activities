import numpy as np
import matplotlib.pyplot as plt

r_earth = 6.371e6 # in meters
m_earth = 5.97e24 # in kg
G = 6.67e-11 # in SI units

radii = np.arange(1,10.1,0.1)
U = -G * m_earth / (radii * r_earth)

plt.plot(radii,U)
plt.xlabel("Distance from center of Earth (Earth Radii)")
plt.ylabel("Potential energy of 1 kg object (J)")
plt.title("Potential energy curve for a 1kg object above the Earth's surface")
plt.xlim(0,10)
plt.show()
