from matplotlib import pyplot as plt    
from matplotlib import pyplot as plt    
percentage = [97,54,45,10, 20, 10, 30,97,50,71,40,49,40,74,95,80,65,82,70,65,55,70,75,60,52,44,43,42,45]    
number_of_student = [0,10,20,30,40,50,60,70,80,90,100]    
plt.hist(percentage, number_of_student, histtype='bar', rwidth=0.8)    
plt.xlabel('percentage')    
plt.ylabel('Number of people')    
plt.title('Histogram')    
plt.show()