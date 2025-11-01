
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os
from scipy.signal import convolve2d

def circular_ring(size=10, inner_radius=3, outer_radius=4):
    center = (size - 1) / 2
    Y, X = np.ogrid[:size, :size]
    dist_from_center = np.sqrt((X - center)**2 + (Y - center)**2)
    ring = np.where((dist_from_center >= inner_radius) & (dist_from_center <= outer_radius), 1, 0)
    return ring

def growth(U):
    # return np.where(((U >= 0.15) & (U <= 0.18)) | ((U >= 0.72) & (U <= 0.85)), 1, -1)
    # return 0 + ((U >= 0.135) & (U <= 0.165)) - ((U < 0.135) | (U > 0.165))
    return 0 + ((U>=0.12)&(U<=0.1481)) - ((U<0.12)|(U>0.1481))

def convolve(data, kernel):
    kr, kc = kernel.shape
    dr, dc = data.shape
    scaled_data = np.tile(data, (3, 3))
    new_data = np.zeros((dr, dc))
    for i in range(dr):
        for j in range(dc):
            if np.sum(kernel) == 0:
                val = 0
            else:
                val = np.sum(scaled_data[int(dr+i-(kr-1)/2):int(dr+i+(kr+1)/2), int((dc+j-(kc-1)/2)):int((dc+j+(kc+1)/2))] * kernel)/np.sum(kernel)
            new_data[i, j] = np.clip(data[i, j] + dt * growth(val), 0, 1)
    return new_data


# Kernel (Can be customized to shape n x n with odd number n)
kernel = np.array([
[0.03, 0.13, 0.22, 0.22, 0.03],
[0.13, 0.61, 0.98, 0.61, 0.13],
[0.22, 0.98, 1, 0.98, 0.22],
[0.13, 0.61, 0.98, 0.61, 0.13],
[0.03, 0.13, 0.22, 0.13, 0.03]])
# 17x17 Gaussian Kernel
kernel = np.array([
 [0.011, 0.018, 0.030, 0.048, 0.073, 0.106, 0.145, 0.183, 0.213, 0.230, 0.230, 0.213, 0.183, 0.145, 0.106, 0.073, 0.048],
 [0.018, 0.030, 0.050, 0.080, 0.119, 0.169, 0.228, 0.285, 0.333, 0.361, 0.361, 0.333, 0.285, 0.228, 0.169, 0.119, 0.080],
 [0.030, 0.050, 0.083, 0.132, 0.194, 0.273, 0.364, 0.454, 0.530, 0.575, 0.575, 0.530, 0.454, 0.364, 0.273, 0.194, 0.132],
 [0.048, 0.080, 0.132, 0.209, 0.308, 0.435, 0.577, 0.718, 0.837, 0.907, 0.907, 0.837, 0.718, 0.577, 0.435, 0.308, 0.209],
 [0.073, 0.119, 0.194, 0.308, 0.451, 0.637, 0.844, 1.044, 1.217, 1.319, 1.319, 1.217, 1.044, 0.844, 0.637, 0.451, 0.308],
 [0.106, 0.169, 0.273, 0.435, 0.637, 0.897, 1.189, 1.469, 1.714, 1.819, 1.819, 1.714, 1.469, 1.189, 0.897, 0.637, 0.435],
 [0.145, 0.228, 0.364, 0.577, 0.844, 1.189, 1.579, 1.949, 2.269, 2.410, 2.410, 2.269, 1.949, 1.579, 1.189, 0.844, 0.577],
 [0.183, 0.285, 0.454, 0.718, 1.044, 1.469, 1.949, 2.405, 2.800, 2.968, 2.968, 2.800, 2.405, 1.949, 1.469, 1.044, 0.718],
 [0.213, 0.333, 0.530, 0.837, 1.217, 1.714, 2.269, 2.800, 3.260, 3.456, 3.456, 3.260, 2.800, 2.269, 1.714, 1.217, 0.837],
 [0.230, 0.361, 0.575, 0.907, 1.319, 1.819, 2.410, 2.968, 3.456, 3.660, 3.660, 3.456, 2.968, 2.410, 1.819, 1.319, 0.907],
 [0.230, 0.361, 0.575, 0.907, 1.319, 1.819, 2.410, 2.968, 3.456, 3.660, 3.660, 3.456, 2.968, 2.410, 1.819, 1.319, 0.907],
 [0.213, 0.333, 0.530, 0.837, 1.217, 1.714, 2.269, 2.800, 3.260, 3.456, 3.456, 3.260, 2.800, 2.269, 1.714, 1.217, 0.837],
 [0.183, 0.285, 0.454, 0.718, 1.044, 1.469, 1.949, 2.405, 2.800, 2.968, 2.968, 2.800, 2.405, 1.949, 1.469, 1.044, 0.718],
 [0.145, 0.228, 0.364, 0.577, 0.844, 1.189, 1.579, 1.949, 2.269, 2.410, 2.410, 2.269, 1.949, 1.579, 1.189, 0.844, 0.577],
 [0.106, 0.169, 0.273, 0.435, 0.637, 0.897, 1.189, 1.469, 1.714, 1.819, 1.819, 1.714, 1.469, 1.189, 0.897, 0.637, 0.435],
 [0.073, 0.119, 0.194, 0.308, 0.451, 0.637, 0.844, 1.044, 1.217, 1.319, 1.319, 1.217, 1.044, 0.844, 0.637, 0.451, 0.308],
 [0.048, 0.080, 0.132, 0.209, 0.308, 0.435, 0.577, 0.718, 0.837, 0.907, 0.907, 0.837, 0.718, 0.577, 0.435, 0.308, 0.209]
])
kernel = kernel/np.sum(kernel)
# Space Width (Height)
size = 100
# Time Interval
dt = 0.1

# Option 1: Random Cell Generation
# data = np.random.rand(size, size)

# Option 2: Circular Ring in Empty Space
data = np.zeros((size, size))
data[40:50, 40:50] = circular_ring()
data[20:30, 70:80] = circular_ring()

# Option 3: Random Cell Generation With Threshold (Limit Cell Number)
# data = np.random.rand(size, size)
# data[data <= 0.95] = 0

fig, ax = plt.subplots()
im = ax.imshow(data)
ax.axis('off')

def init():
    im.set_data(data)
    return[im]

def animate(i):
    next_frame = convolve(im.get_array(), kernel)
    # next_frame = np.clip(im.get_array() + dt * growth(convolve2d(im.get_array(), kernel, mode='same', boundary='wrap')), 0, 1)
    im.set_data(next_frame)
    return [im]

anim = FuncAnimation(fig, animate, init_func=init, frames=100, interval=5, blit=True)
os.chdir('/Users/albertdai/Desktop')
anim.save('animation.mp4', writer='ffmpeg', fps=30)
plt.show()