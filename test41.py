from matplotlib import pyplot as plt    
from matplotlib import style    
style.use('ggplot')    
    
x = [4,8,12]    
y = [19,11,7]    
    
x2 = [7,10,12]    
y2 = [8,18,24]    
    
plt.scatter(x, y)    
    
plt.scatter(x2, y2, color='g')    
    
plt.title('Epic Info')    
plt.ylabel('Y axis')    
plt.xlabel('X axis')    
    
plt.show()   