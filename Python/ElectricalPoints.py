import numpy as np
import matplotlib.pyplot as plt

# constants
g = 9.81 # m/s^2
permitivity = 8.854e-12 # C^2/(N*m^2)
coulomb = 1.602e-19 # C
electric_charge = -1 * coulomb # C
electron_mass = 9.11e-31 # kg

#initial conditions
x, y = 5.5e-4, 5.5e-4 # meters
x_velocity, y_velocity = 0.0, 0.0 # m/s

x_points, y_points = [x], [y]

# time variables
t_start = 0 # seconds
t_end = 5 # seconds
dt = 0.1 # seconds
time = np.arange(t_start, t_end, dt)

# update loop
for t in time[1:]:
    #radial unit vector
    r_magnitude = np.sqrt(x**2 + y**2)
    r_hatx = x / r_magnitude
    r_haty = y / r_magnitude

    # electric field
    E_magnitude = 1.602e-19 / (4 * np.pi * permitivity * r_magnitude**2)
    Ex = E_magnitude * r_hatx
    Ey = E_magnitude * r_haty

    # acceleration
    ax = (electric_charge * Ex) / electron_mass
    ay = (electric_charge * Ey) / electron_mass

    # velocity update
    x_velocity += ax * dt
    y_velocity += ay * dt

    # position update
    x += x_velocity * dt
    y += y_velocity * dt
    x_points.append(x)
    y_points.append(y)

# visualitation graphing
fig, ax = plt.subplots()
plt.plot(x_points, y_points,linewidth=3,linestyle='--' , label='Point Charge 1 Position')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.grid()
plt.show()