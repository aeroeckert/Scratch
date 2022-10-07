import numpy as np
import matplotlib.pyplot as plot
import time

tstart = time.time()
plot.subplot(1,1,1)

plot.axis([0, 10, 0, 1])

for i in range(100):
    if (i%10 != 0):
        y = np.random.random()
        plot.scatter(i, y)
        plot.pause(0.1)
    else:
        plot.cla()
        

plot.show()