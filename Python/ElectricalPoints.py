import numpy as np
import matplotlib.pyplot as plt

# constants
g = 9.81 # m/s^2
permitivity = 8.854e-12 # C^2/(N*m^2)
coulomb = 1.602e-19 # C
electric_charge = 1 * coulomb # C

# User inputs for point charge 1
pointx_input = input("Enter x coordinate of point charge 1 (m): ")
pointy_input = input("Enter y coordinate of point charge 1 (m): ")
point_velocity_input = input("Enter velocity of point charge 1 (m/s): ")

pointx = float(pointx_input)
pointy = float(pointy_input)
point_velocity = float(point_velocity_input)

# time variables
t_start = 0 # seconds
t_end = 5 # seconds
dt = 0.1 # seconds
time = np.arange(t_start, t_end, dt)

# position calculations
x_position = pointx + point_velocity * time
y_position = pointy + 0 * time  # assuming no vertical movement


# visualitation graphing
fig, ax = plt.subplots()
plt.plot(x_position, y_position,linewidth=3,linestyle='--' , label='Point Charge 1 Position')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.grid()
plt.show()