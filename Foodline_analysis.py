import numpy.random as rnd
import numpy
import pandas as pd
import matplotlib.pyplot as plt

res = 1/3

hoods = [1, res, res+res**2]

for x in range(12):
    #correction factor for already existing
    x += 3

    hoods.append(res*(hoods[x-3] + hoods[x-2] + hoods[x-1]))


#plotting just the people in third position + (x+1) to correct for useless firster
graf = pd.DataFrame([ hoods[x] for x in range(1,len(hoods)) if (x+2)%3 == 0])

graf.plot(kind = "line")

plt.show()