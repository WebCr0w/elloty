import numpy as np
def GenChis(h=1,k=0):
 B=[]
 for g in range(0,h):
  A=np.random.randint(100)
  B.append(A+k)
 return B
from matplotlib import pyplot as plt
rand=['rand1', 'rand2', 'rand3', 'rand4', 'rand5', 'rand6']
value=GenChis(len(rand))
xs=[i+0.1 for i, _ in enumerate(rand)]
plt.bar(xs, value)
plt.ylabel('Столбцы')
plt.title('Название')
plt.xticks([i + 0.1 for i, _ in enumerate(rand)], rand)
plt.show()
        
