import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from matplotlib.widgets import Slider
from scipy.stats import poisson


def function(la,x):
    return np.exp(-la)*np.power(la,x)/factorial(x)

x = np.arange(0,20,0.1)
fig, ax = plt.subplots()
line, = ax.plot(x, function(5,x), lw=2)
ax.set_ylim(0,0.3)

fig.subplots_adjust(left=0.25, bottom=0.25)
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(
    ax = axfreq,
    label='Lambda',
    valmin= 0,
    valmax= 10,
    valinit = 5
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

lower_cdf = poisson.cdf(k=0, mu=5)
higher_cdf = poisson.cdf(k=0, mu=5)

net_cdf = higher_cdf-lower_cdf
text = ax.text(16.2, 0.242, 'Mean: '+str(round(slider.val,2))+'\n'+'Var:    '+str(round(slider.val,2))+'\n'+'C.D.F: '+str(round(net_cdf,2)), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})



def update(val):
    ax.fill_between([0,20], [0.3,0.3], facecolor='white', alpha=1)
    Y = function(slider.val,x)
    line.set_ydata(Y)
    ax.fill_between(x,Y, 0, where= (x >= cdf_slider_lower.val)&(x <= cdf_slider.val) )
    #Artist.set_visible(ax.text, False)
    lower_cdf = poisson.cdf(k=cdf_slider_lower.val, mu=slider.val)
    higher_cdf = poisson.cdf(k=cdf_slider.val, mu=slider.val)
    total_cdf = higher_cdf-lower_cdf
    total_cdf = max(0,total_cdf)
    text.set_text('Mean: '+str(round(slider.val,2))+'\n'+'Var:    '+str(round(slider.val,2))+'\n'+'C.D.F: '+str(round(total_cdf,2)))

    fig.canvas.draw_idle()
    

slider.on_changed(update)
cdf_slider.on_changed(update)
cdf_slider_lower.on_changed(update)
plt.show()
