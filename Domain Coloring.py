import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#45 seconds

resolution = width, height = 2*(1000,)

xmin, xmax = -5, 5
xwidth = xmax - xmin

ymin, ymax = -5, 5
yheight = ymax - ymin

x,y = np.ogrid[xmin:xmax:1j*width, ymin:ymax:1j*height]

cp = (x + 1j*y).T

def f(z):
    return z

fig = plt.figure()

ax = fig.add_subplot(121)
im = ax.pcolormesh(np.angle(f(cp)), cmap = cm.hsv)

ax2 = fig.add_subplot(122)
im2 = ax2.pcolormesh(abs(f(cp)), cmap = cm.plasma)

cbar = fig.colorbar(ax=ax2, mappable=im2, orientation='vertical')
cbar = fig.colorbar(ax=ax, mappable=im, orientation='vertical')

xtick_labels = np.linspace(xmin, xmax, 7, endpoint=True)
ax.set_xticks([(x-xmin)*(width)/(xwidth) for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
ax2.set_xticks([(x-xmin)*(width)/(xwidth) for x in xtick_labels])
ax2.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])

ytick_labels = np.linspace(ymin, ymax, 7, endpoint=True)
ax.set_yticks([(y-ymin)*(height)/(yheight) for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])
ax2.set_yticks([(y-ymin)*(height)/(yheight) for y in ytick_labels])
ax2.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])

ax.set_title('Argument of $f(z)$')
ax2.set_title('Magnitude of $f(z)$')


plt.show()