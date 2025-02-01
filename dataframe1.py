import numpy as np
import matplotlib.pyplot as plt
objects = ('python' , 'c++', 'java' , 'perl' , 'scale' , 'lisp')
y_pos = np.arange ( len ( objects ) )
performance = [10, 8, 6, 4, 2, 1]
plt.barh(y_pos, performance, align = "center", color='r')
plt.yticks(y_pos, objects)
plt.xlabel("usage")
plt.title('programming language usage')
plt.show()
