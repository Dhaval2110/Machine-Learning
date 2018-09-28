import numpy as np
import matplotlib.pyplot as plt
"""
x=[1,2,3,4,5]
y=[100,200,300,400,500]

plt.bar(x,y)
plt.show()
"""

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
plt.show()


