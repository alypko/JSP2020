import numpy as np
import matplotlib.pyplot as plt

labels = ['C','Java','Python','C++','C#','Visual Basic','JavaScript','PHP']
values = [17.38, 11.96, 11.72, 7.56, 3.95, 3.84, 2.20, 1.99]

plt.bar(labels,values)
plt.title("Popularność wybranych języków programowania")
plt.xlabel('popularność [%]')
plt.ylabel('języki program.')
plt.show()