import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from matplotlib.widgets import Slider
from scipy.stats import poisson
from turtle import color
from scipy.stats import uniform
from scipy.stats import norm

def uniform_fun(x,a,b):
    return uniform.pdf(x,a,b-a)


x = np.arange(0,20,0.1)
fig, ax = plt.subplots()
line, = ax.plot(x, uniform_fun(x,0,1), lw=2)

y_lim_list = [1,0.3,0.6]
ax.set_ylim(0,1.5)

fig.subplots_adjust(left=0.25, bottom=0.3)
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(
    ax = axfreq,
    label='a',
    valmin= 0,
    valmax= 10,
    valinit = 0
)

axfreq = fig.add_axes([0.25, 0.2, 0.65, 0.03])
slider2 = Slider(
    ax = axfreq,
    label='b',
    valmin= 0,
    valmax= 10,
    valinit = 1
)

axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
cdf_slider = Slider(
    ax=axamp,
    label="upper",
    valmin=0,
    valmax=20,
    valinit=0,
    orientation="vertical"
)


axamp = fig.add_axes([0.02, 0.25, 0.0225, 0.63])
cdf_slider_lower = Slider(
    ax=axamp,
    label="lower",
    valmin=0,
    valmax=20,
    valinit=0,
    orientation="vertical"
)



lower_cdf = 0.0
higher_cdf = 0.0
expected_value = 0.5
var = 0.08
net_cdf = higher_cdf-lower_cdf
text = ax.text(16.2, 1.2, 'Mean: '+str(expected_value)+'\n'+'Var:    '+str(var)+'\n'+'C.D.F: '+str(round(net_cdf,2)), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

def update(val):
    ax.fill_between([0,10], [1.5,1.5], facecolor='white', alpha=1)
    a = slider.val
    #alpha = slider2.val
    b = slider2.val
    b = max(b,0)
    Y = uniform_fun(x,a,b)
    line.set_ydata(Y)
    ax.fill_between(x,Y, 0, where= (x >= cdf_slider_lower.val)&(x <= cdf_slider.val) )
    #Artist.set_visible(ax.text, False)
    x_value = cdf_slider.val
    if x_value > b:
        x_value = b
    elif x_value < a:
        x_value = a
    
    upper_area = (x_value-a)/(b-a)
    y_value = cdf_slider_lower.val
    if y_value > b:
        y_value = b
    elif y_value < a:
        y_value = a
    
    lower_area = (y_value-a)/(b-a)
    total_cdf = upper_area-lower_area
    total_cdf = max(0,total_cdf)
    expected_value = (a+b)/2
    var = (b-a)*(b-a)/12
    text.set_text('Mean: '+str(round(expected_value,2))+'\n'+'Var:    '+str(round(var,2))+'\n'+'C.D.F: '+str(round(total_cdf,2)))

    fig.canvas.draw_idle()
    

slider.on_changed(update)
slider2.on_changed(update)
cdf_slider.on_changed(update)
cdf_slider_lower.on_changed(update)
plt.show()