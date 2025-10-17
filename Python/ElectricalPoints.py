import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#input parameters for particle 1
initial_velocity = input("Enter the initial velocity (m/s): ")
angle_degrees = input("Enter the angle of launch (degrees): ")
angle_radians = np.radians(float(angle_degrees))
initial_velocity_x = float(initial_velocity) * np.cos(angle_radians)
initial_velocity_y = float(initial_velocity) * np.sin(angle_radians)

# constants
g = 9.81 # m/s^2
permitivity = 8.854e-12 # C^2/(N*m^2)
coulomb = 1.602e-19 # C
electric_charge = -1 * coulomb # C
electron_mass = 9.11e-31 # kg

#initial conditions particle 1
x, y = 10, 10 # meters
x_velocity, y_velocity = initial_velocity_x, initial_velocity_y # m/s

x_points, y_points = [x], [y]

# time variables
t_start = 0 # seconds
t_end = 15 # seconds
dt = 0.001 # seconds
time = np.arange(t_start, t_end, dt)

# update loop
for t in time[1:]:
    #radial unit vector
    r_magnitude = np.sqrt(x**2 + y**2)
    r_hatx = x / r_magnitude
    r_haty = y / r_magnitude

    # electric field
    E_magnitude = 10*1.602e-19 / (4 * np.pi * permitivity * r_magnitude**2)
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

# animation graphing
fig, ax = plt.subplots()
ax.set_xlim(min(x_points), max(x_points))
ax.set_ylim(min(y_points), max(y_points))
animated_plot, = ax.plot([], [])

def update_data(frame):
    animated_plot.set_data(x_points[:frame], y_points[:frame])
    return animated_plot,

animation = FuncAnimation(
    fig=fig,
    func=update_data,
    frames = 15000,
    interval=.001,
    repeat=False
    )
plt.show()