from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mainxyz1

#xpoint=[]
#ypoint=[]
#zpoint=[]

#fig = plt.figure(figsize=(10, 7))
#ax = plt.axes(projection="3d")

##def plot_point3D(x,y,z):
##    # Creating figure
## 
##    # Creating plot
##    ax.scatter3D(xpoint, ypoint, zpoint, color="green")
##    plt.title("3D point clouds")
##    ax.set_xlabel('x')
##    ax.set_ylabel('y')
##    ax.set_zlabel('z')
##    # show plot
##    #plt.show()


def update(frame):
    x,y,z=mainxyz.read_from_port('COM9')
    xpoint.append(x)
    ypoint.append(y)
    zpoint.append(z)
    ax.clear()
    ax.scatter3D(xpoint, ypoint, zpoint, color="green")
    plt.title("3D point clouds")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    fig.canvas.draw()

anim=FuncAnimation(fig,update0)
plt.show()


