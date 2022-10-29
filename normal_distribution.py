import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import norm



def function(x,mean,var):
    return norm.pdf(x,mean,var)

x = np.arange(0,20,0.1)
fig, ax = plt.subplots()
line, = ax.plot(x, function(x,0,1), lw=2)
ax.set_ylim(0,0.5)

fig.subplots_adjust(left=0.25, bottom=0.3)
axfreq = fig.add_axes([0.25, 0.2, 0.65, 0.03])
slider = Slider(
    ax = axfreq,
    label='mean',
    valmin= 0,
    valmax= 10,
    valinit = 0
)


axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider2 = Slider(
    ax = axfreq,
    label='var',
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

lower_cdf = norm.cdf(0,0,1)
higher_cdf = norm.cdf(0,0,1)

net_cdf = higher_cdf-lower_cdf
text = ax.text(16.2, 0.242, 'Mean: 0.0'+'\n'+'Var:    1.0'+'\n'+'C.D.F: '+str(round(net_cdf,2)), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})



def update(val):
    ax.fill_between([0,20], [0.3,0.3], facecolor='white', alpha=1)
    Y = function(x,slider.val,slider2.val)
    line.set_ydata(Y)
    ax.fill_between(x,Y, 0, where= (x >= cdf_slider_lower.val)&(x <= cdf_slider.val) )
    #Artist.set_visible(ax.text, False)
    lower_cdf = norm.cdf(cdf_slider_lower.val,slider.val,slider2.val)
    higher_cdf = norm.cdf(cdf_slider.val,slider.val,slider2.val)
    total_cdf = higher_cdf-lower_cdf
    total_cdf = max(0,total_cdf)
    text.set_text('Mean: '+str(round(slider.val,2))+'\n'+'Var:    '+str(round(slider2.val,2))+'\n'+'C.D.F: '+str(round(total_cdf,2)))

    fig.canvas.draw_idle()
    

slider.on_changed(update)
slider2.on_changed(update)
cdf_slider.on_changed(update)
cdf_slider_lower.on_changed(update)
plt.show()


