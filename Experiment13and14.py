import numpy as np
x = np.random.randint(100, size=(6,4))
print(x)
newarr = x.reshape(4,6)
print(newarr)
x.resize(3,8)
print(x)


"""maxelement = x.max()
maxindex = np.where(x==maxelement)
minelement = x.min()
minindex = np.where(x==minelement)
print(f"Maximum element is {maxelement} and index is {maxindex}")
print(f"Maximum element is {minelement} and index is {minindex}")"""
