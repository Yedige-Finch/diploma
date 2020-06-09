import matplotlib.pyplot as plt
x = [0.1]
I = [0]
R = 1
D = 1
g = 0.4645
for i in range(0,50):
    x.append(R*(1-x[i]/D)**(-g))
    I.append(i)
plt.plot(I,x)
plt.show()