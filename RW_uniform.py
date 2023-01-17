import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

N = 1000
x = [[0,0]] # lintasan posisi partikel
xs = [0,0] # posisi awal partikel

# perulangan untuk mengubah posisi partikel secara default berdasarkan 5 arah yang ditentukan
# kiri, atas, tetap, bawah, kanan
movement = [[-1,0], [1,0], [0,0], [0,-1], [0,1]]
for i in range(N):
  rd = random.choices(movement,[1,1,1,1,1], k=1)[0]
  x.append([xs[0]+rd[0],xs[1]+rd[1]])
  xs[0] = xs[0]+rd[0] 
  xs[1] = xs[1]+rd[1] 

# Visualisasi
x = np.array(x)
xmin = np.min(np.array(x)[:,0])
xmax = np.max(np.array(x)[:,0])
ymin = np.min(np.array(x)[:,1])
ymax = np.max(np.array(x)[:,1])

def animate(i):
  ax.clear()
  ax.set_xlim(xmin-1,xmax+1)
  ax.set_ylim(ymin-1,ymax+1)
  ax.plot(x[:i,0], x[:i,1])

fig,ax = plt.subplots(1, figsize = (5,5))
ani = FuncAnimation(fig, animate, frames=N, interval=100)
plt.show()