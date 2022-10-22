import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from matplotlib.widgets import Slider
from scipy.stats import poisson
from turtle import color

from scipy.stats import expon

def function(la,x):
    return np.exp(-la)*np.power(la,x)/factorial(x)

def exponential(x,scale):
    return expon.pdf(x,0,scale)

x = np.arange(0,20,0.1)
fig, ax = plt.subplots()
line, = ax.plot(x, function(5,x), lw=2)
line2, = ax.plot(x,exponential(x,0.2),'r-',lw=2)
ax.set_ylim(0,0.6)

fig.subplots_adjust(left=0.25, bottom=0.25)
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(
    ax = axfreq,
    label='Lambda',
    valmin= 0,
    valmax= 10,
    valinit = 5
)


def update(val):
    
    Y = function(slider.val,x)
    Y2 = exponential(x,1/slider.val)
    line.set_ydata(Y)
    line2.set_ydata(Y2)
    fig.canvas.draw_idle()
    

slider.on_changed(update)

plt.show()
