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

#animation #3
for i in range(0,120):
       A=-0.153-float(i)*0.008
       B=-0.895+float(i)*0.006
       #A=np.sin(float(-i*0.01)+180.0/np.pi)-0.15
       #B=-np.cos(float(-i*0.01))-0.15
       C=-0.05-float(i)*0.003
       x=np.linspace(0.0, 10.0, num=100)
       y=A*np.exp(-((x-2.0)**2)/0.8)+B*np.exp(-((x-8.0)**2)/0.8)+C*np.exp(-((x-5.0)**2)/0.6)
       print i, A, B, C, A/B, C/B, B/B

       plt.ylim(-1.25,0.6)
       plt.plot(x,y,color='black',lw=2.0)
       plt.axis('off')
       plt.savefig('DnaK_animation_test/out%i.png'%i, dpi=300)
       plt.close()

