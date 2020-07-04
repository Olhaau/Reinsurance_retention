import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fac = np.math.factorial
e = np.e

# uses a pareto distribution as model for the claim distribution
def F_par(x,k,m):
    res = 0
    if (x > m): res = 1 - (m / x) ** k
    return res

n = 100
m = 1
k = .9
f =(lambda x: F_par(x + 1.0, k, m) - F_par(x, k, m))
ran =  np.arange(0,5,.01)
#plt.plot(ran,[F_par(x, 3, 1) for x in ran])


value = list(range(50000,1050000, 10000))
dist = [f(x) for x in range(1,100)]
dist.append(1-F_par(100,k,m))
print(len(dist),sum(dist), len(value))
#plt.bar(value,dist)
#plt.show()

#print(dist,value)
df = pd.DataFrame({'value':value,'dist': dist})
print(df.head())

df.to_excel("synthetic_claim_size_dist.xlsx")
