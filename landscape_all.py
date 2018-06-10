# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:39:17 2018

@author: caenglish
"""

#!/bin/python

import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import matplotlib.patches as mpatches

#apo/ADP-bound to substrate, animation #1
for i in range(0,70):
       fig, ax = plt.subplots()
#       patches = []
       ax.set_ylim(-1.25,0.6)
       ax.set_xlim(0,10)
       #Original positions ()

       wedge = mpatches.Polygon(np.array([[0.84,0.88],[0.98,0.88],[0.98,0.80]]),fc='blue',ec='None',transform=ax.transAxes)
       plt.arrow(0.844+float(i)*0.00195, 0.973, 0.0,-0.06, head_width=0.02, head_length=0.03,color='black',transform=ax.transAxes)
       
       ax.add_patch(wedge)
       A=-0.60-float(i)*0.003
       B=-0.15
       C=-0.05-float(i)*0.004
       x=np.linspace(0.0, 10.0, num=100)
       y=A*np.exp(-((x-2.0)**2)/0.8)+B*np.exp(-((x-8.0)**2)/0.8)+C*np.exp(-((x-5.0)**2)/0.6)
       print(i, A, C,B,0.86-float(i)*0.0037,0.96-float(i)*0.0037)
       
       
       plt.plot(x,y,color='black',lw=2.0)
       plt.axis('off')
       plt.savefig('out%i.png'%i, dpi=300)
       plt.close()
