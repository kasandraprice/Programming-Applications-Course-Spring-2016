import matplotlib.pyplot as plt #import matlibplots 
plt.rcdefaults()
import numpy as np   #import numpy
from numpy import sin,cos,pi # add label cos, sin and pi 

a = np.linspace(0,6*pi,100) #set array from 0 to 6pi 
y_sin=sin(a)  #calculate y for sine 
y_cos=cos(a)  #calculate x for cosine 

plt.gca().set_color_cycle(['blue','red']) # estbalish the color for the lines of the graph 
plt.plot(a,y_sin, '--')  # set plot for  sin 
plt.plot(a,y_cos)  #set plot for cos
plt.ylabel("y")    #label y-axis
plt.xlabel("x")    #label x-axis

def get_color():   # set color for graph 
    for item in ['r','b']:
        yield item
color= get_color()

plt.legend(('sin(x)', 'cos(x)')) #add legend 
plt.title('Plot of sin(x) and cos(x) from 0 to 6pi')

plt.show()
# Kasandra Price
#@02754360
#01/21/2016
