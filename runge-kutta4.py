import math as maths
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib import cm
from matplotlib.animation import FuncAnimation
import time

def RK4(t, x, y, z, dt, f, direction):
    if direction == 'x':
        k1 = f(t, x, y, z)
        k2 = f(t+dt/2,x+k1*dt/2, y, z)
        k3 = f(t+dt/2, x+k2*dt/2, y, z)
        k4 = f(t+dt, x+k3*dt, y, z)
    elif direction == 'y':
        k1 = f(t, x, y, z)
        k2 = f(t+dt/2, x, y+k1*dt/2, z)
        k3 = f(t+dt/2, x, y+k2*dt/2, z)
        k4 = f(t+dt, x, y+k3*dt, z)
    elif direction == 'z':
        k1 = f(t, x, y, z)
        k2 = f(t+dt/2, x, y, z+k1*dt/2)
        k3 = f(t+dt/2, x, y, z+k2*dt/2)
        k4 = f(t+dt, x, y, z+k3*dt)
    return k1+2*(k2+k3)+k4

def xD1(t, x, y, z):
    return 10*(y-x)

def yD1(t, x, y, z):
    return x*(28-z)-y

def zD1(t, x, y, z):
    return x*y-8/3*z

def lorenzRK4(t, x, y, z, dt, domain):
    points = [[t, x, y, z]]
    for i in range(int(domain/dt)):
        x, y, z = x+dt/6*RK4(t, x, y, z, dt, xD1, 'x'), y+dt/6*RK4(t, x, y, z, dt, yD1, 'y'), z+dt/6*RK4(t, x, y, z, dt, zD1, 'z')
        points.append([t,x,y,z])
        t += dt
    return np.array(points)

plt.style.use('dark_background')
plot = lorenzRK4(0, 1, 1, 14, 0.005, 60)
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection = '3d')
ax.scatter3D(np.array([i[1] for i in plot]), np.array([i[2] for i in plot]), np.array([i[3] for i in plot]), s=1, c=np.array([i[0] for i in plot]), cmap='RdPu_r')
plt.show()

