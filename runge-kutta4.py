import math as maths
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib import cm
from matplotlib.animation import FuncAnimation
import time

def RK4(t, x, y, z, dt, f, direction): ## This calculates the derivatives at different points of the function and then returns a weighted average
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

def xD1(t, x, y, z): ## dx/dt
    return 10*(y-x)

def yD1(t, x, y, z): ## dy/dt
    return x*(28-z)-y

def zD1(t, x, y, z): ## dz/dt
    return x*y-8/3*z

def RK4loop(t, x, y, z, dt, domain): ## This is the loop that actually does the runge-kutta method
    points = [[t, x, y, z]]
    for i in range(int(domain/dt)):
        x, y, z = x+dt/6*RK4(t, x, y, z, dt, xD1, 'x'), y+dt/6*RK4(t, x, y, z, dt, yD1, 'y'), z+dt/6*RK4(t, x, y, z, dt, zD1, 'z')
        points.append([t,x,y,z])
        t += dt
    return np.array(points)

def update(frame): ## used for animation
    print(f'{100*step*frame/len(plots[0])}%')
    for i in range(n):
        x = plots[i][frame, 1]
        z = plots[i][frame, 3]
        ax.plot(x, z, linewidth=0.5, color=colours[i])

## Everything here is used for displaying the plot
plt.style.use('dark_background')
n = 20
plots = [RK4loop(0, 1-2*i/(n-1), 0, 0, 0.001, 60) for i in range(n)]
step = 2
plots = [np.array([plot[step*i] for i in range(10000, len(plot)//step)]) for plot in plots]
colours = [(1-i/(n-1), 0.73*i/(n-1), 1) for i in range(n)]
#fig = plt.figure(figsize = (10, 7))
#ax = plt.axes(projection = '3d')
fig, ax = plt.subplots()
fig.set_dpi(1200)
plt.axis('off')
#ax.set_xlim([-25, 25])
#ax.set_ylim([0, 60])
for i in range(n):
    plt.plot(plots[i][:,1], plots[i][:,3], linewidth=1, color=colours[i])
#extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
#plt.savefig("test.png", bbox_inches=extent, dpi=500)
plt.show()
#ani.save(filename="lorenz.mp4", writer="ffmpeg", dpi=500)
# for i in range(len(plots)):
#     plot = plots[i]
#     plt.plot(plot[:,1], plot[:,3], color=colours[i])
