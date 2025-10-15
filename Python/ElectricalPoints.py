import numpy as np

# constants
g = 9.81 # m/s^2
permitivity = 8.854e-12 # C^2/(N*m^2)
coulomb = 1.602e-19 # C
electric_charge = 1 * coulomb # C

pointx_input = input("Enter x coordinate of point charge 1 (m): ")
pointy_input= input("Enter y coordinate of point charge 1 (m): ")

pointx2_input= input("Enter x coordinate of point charge 2 (m): ")
pointy2_input= input("Enter y coordinate of point charge 2 (m): ")

pointx = float(pointx_input)
pointy = float(pointy_input)

pointx2 = float(pointx2_input)
pointy2 = float(pointy2_input)

distance = np.sqrt((pointx2-pointx)**2 + (pointy2-pointy)**2)
ForceE = (1/(4*np.pi*permitivity)) * (electric_charge**2/(distance**2))

print(distance)
print(ForceE)