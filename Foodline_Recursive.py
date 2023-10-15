import numpy.random as rnd
import numpy
import pandas as pd
import matplotlib.pyplot as plt

res = 1/3

hoods = [1, res, res+res**2]

for x in range(12000):
    #correction factor for already existing
    x += 3

    hoods.append(res*(hoods[x-3] + hoods[x-2] + hoods[x-1]))

graf = pd.DataFrame(hoods[1:])

graf.to_csv("Likelihood_recursive.csv")

graf.plot(kind = "bar")

plt.show()