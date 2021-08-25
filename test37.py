from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
x=[10,12,13]
y=[8,16,6]
x2=[8,15,11]
y2=[6,15,7]

plt.plot(x,y,'b',label='lineone',linewidth=5)
plt.plot(x2,y2,'r',label='linetwo',linewidth=5)
plt.title('Epic Info')

# fig=plt.figure()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()