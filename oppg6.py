import numpy as np
import math
import scipy.stats as stats

data = np.genfromtxt('salmonella', delimiter=',', dtype=float)

n = len(data)

sum_data_2 = 0
for i in data:
    sum_data_2 += math.pow(i, 2)

mu_hat = float(sum(data) / n)

# Calculates sigma squared and sigma
sigma_2 = (sum_data_2 - (n * math.pow(mu_hat, 2))) / (n - 1)
sigma = math.sqrt(sigma_2)

alpha_input = float(input('Skriv inn konfidensintervall prosent: '))
alpha = 1 - (alpha_input/100)

chi_lower = stats.chi2.isf(alpha/2, (n-1))
chi_upper = stats.chi2.isf(1-alpha/2, (n-1))

lower_limit = math.sqrt(((n-1)*sigma_2)/chi_lower)
upper_limit = math.sqrt(((n-1)*sigma_2)/chi_upper)

print('Punktestimat for standardavvik: ', round(sigma,2))
print('%d%% konfidensintervall: \n' '[%s , %s]' % (alpha_input, round(lower_limit, 2), round(upper_limit,2)))
