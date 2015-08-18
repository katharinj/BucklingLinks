'''
Created on Aug 17, 2015

@author: Rebecca
'''
print "hello"



# here is how to make a matplotlib graph of a parabola
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,1,10)
y=x**2
plt.plot(x,y)
plt.axis([-1,1,0,1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("my first plot")
plt.show()



# here is how to create an animation of y=a x^2 for various a values.
from matplotlib import animation
fig=plt.figure()  #names the figure
ax=plt.axes(xlim=(-1,1),ylim=(0,4))
line, = ax.plot([],[],lw=2) 
#above, the comma says it's a special data type, 
#and this line creates an empty line object (with no data)

def init():
    line.set_data([],[])
    return line,

#animation function. This is called sequentially
def animate(i):
    amax=4
    imax=100
    a=amax*i/imax
    x=np.linspace(-1,1,20)
    y= a*x**2
    line.set_data(x,y)
    return line,

anim=animation.FuncAnimation(fig, animate,init_func=init,frames=100,interval=20,blit=True)
plt.show()