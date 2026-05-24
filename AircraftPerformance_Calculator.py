import numpy as np
import matplotlib.pyplot as plt

# Aircraft and flight condition asssumptions

rho = 1.225     # airdensity at sea level, kg/m^3
V = 70          # velocity, m/s
s = 16.2        # Wing Area, m^2
CL = 0.8        # Coeffecient of lift
CD = 0.045      # Coeffecient of drag
W = 11000       # aircraft weight, N
cl_max = 1.5    # maximum lift coeffecient
mu = 1.81e-5    # diynamic viscosity of air, kg/(m*s)
c = 1.5         # chord length, m
a = 343         # speed of sound at sea level, m/s

# Aircraft performance calculations

lift = 0.5 * rho * V**2 * s * CL
drag = 0.5 * rho * V**2 * s * CD
mach = V / a
reynolds_number = (rho * V * c) / mu
stall_speed = np.sqrt((2 * W) / (rho * 5 * cl_max))

# print results
print("Aircraft perforance summary")
print("----------------")
print("velocity:", V, "m/s")
print("Lift:", round(lift,2),"N")
print("Drag:", round(drag,2),"N")
print("Mach number:", round(mach,3))
print("Reynolds number:", "{:.2e}".format(reynolds_number))
print("Stall speed:", round(stall_speed,2), "m/s")

# Velocity range for graphing 
velocity_range = np.linspace(20, 120, 100)

# Lift and drag values accross the velocity range
lift_values = 0.5 * rho * velocity_range**2 * s * CD
drag_values = 0.5 * rho * velocity_range**2 * s * CD

# Plot lift vs velocity
plt.figure(figsize=(8, 5))
plt.plot(velocity_range, lift_values)
plt.xlabel("velocity_range,(m/s)")
plt.ylabel("lift (N)")
plt.title("lift vs. velocity")
plt.grid(True)
plt.show()

#Plot drag vs. velocity
plt.figure(figsize=(8,5))
plt.plot(velocity_range, drag_values)
plt.xlabel("velocity (m/s)")
plt.ylabel("drag (N)")
plt.title("drag vs. velocity")
plt.grid(True)
plt.show()

