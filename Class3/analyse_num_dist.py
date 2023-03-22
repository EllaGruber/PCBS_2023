#! /usr/bin/env python
# Time-stamp: <2021-03-23 21:36:06 christophe@pallier.org>

import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1], comment='#')

plt.scatter(data['distance'], data['RT'])
plt.title('Distance effect')
plt.xlabel('Distance from threshold')
plt.ylabel('Reaction Time')
plt.savefig("Distance_effect.png")

plt.show()
