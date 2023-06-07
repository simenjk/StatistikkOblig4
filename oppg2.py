import numpy as np
import statsmodels.graphics.gofplots as plots
import matplotlib.pyplot as plt

# The cat's weight in kg
bwt = np.genfromtxt('katters_vekt.csv', skip_header=1, delimiter=',', usecols=2)
# Heart weight in g
hwt = np.genfromtxt('katters_vekt.csv', skip_header=1, delimiter=',', usecols=3)

# Plots cat's weight with QQ-plot
qq_bwt = plots.qqplot(bwt, line='s')
plt.title('Vekt - Katt')
plt.show()

# Plots heart's weight with QQ-plot
qq_hwt = plots.qqplot(hwt, line='s')
plt.title('Vekt - Hjerte')
plt.show()





