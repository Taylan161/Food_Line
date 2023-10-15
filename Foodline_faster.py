import numpy.random as rnd
import numpy
import pandas as pd
import matplotlib.pyplot as plt


# size of the result numpy array
result = numpy.array([0 for x in range(12)])

for x in range(500000):

    holder = numpy.array([])

    while len(holder) < 16:

        res = rnd.randint(0, 3)

        if res == 0:

            holder = numpy.append(holder, [0, 0, 1])

        elif res == 1:

            holder = numpy.append(holder, [0, 1])

        else:

            holder = numpy.append(holder, 1)

    #cutting the calculated results to size, holder slice should be of same size as res
    result = result + numpy.array(holder[:12])

rel = (result/500000)

graph = pd.DataFrame(rel)

graph.to_csv("Foodline_abs.csv")

"""

graph.plot(kind = "bar")

plt.show()
"""