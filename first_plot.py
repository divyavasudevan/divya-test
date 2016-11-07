import matplotlib.pyplot as plt
x=[1,3,5,7,9]
y=[5,6,7,8,9]
x1=[2,4,6,8,10]
y1=[3,4,5,6,7]

plt.bar(x,y,label='Bar 1',color ='g')
plt.bar(x1,y1,label='Bar 2',color = 'r')
plt.title('My first bar graph')
plt.xlabel('Number 1')
plt.ylabel('Number 2')
plt.grid()
plt.legend()
plt.show()
