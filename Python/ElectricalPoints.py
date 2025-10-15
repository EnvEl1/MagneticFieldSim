import numpy as np
import matplotlib.pyplot as plt

# constants
g = 9.81 # m/s^2
permitivity = 8.854e-12 # C^2/(N*m^2)
coulomb = 1.602e-19 # C
electric_charge = 1 * coulomb # C

# User inputs for point charge 1
point_velocity_input = input("Enter velocity of point charge 1 (m/s): ")
point_velocity_angle_input = input("Enter angle of point charge 1 (degrees): ")

point_velocity = float(point_velocity_input)
point_velocity_angle = float(point_velocity_angle_input)

def deg_to_rad(degrees):
    return degrees * (np.pi / 180)

velocity_x = point_velocity * np.cos(deg_to_rad(point_velocity_angle))
velocity_y = point_velocity * np.sin(deg_to_rad(point_velocity_angle))

# time variables
t_start = 0 # seconds
t_end = 5 # seconds
dt = 0.1 # seconds
time = np.arange(t_start, t_end, dt)

# position calculations
x_position = velocity_x * time
y_position = velocity_y * time  # assuming no vertical movement


# visualitation graphing
fig, ax = plt.subplots()
plt.plot(x_position, y_position,linewidth=3,linestyle='--' , label='Point Charge 1 Position')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.grid()
plt.show()