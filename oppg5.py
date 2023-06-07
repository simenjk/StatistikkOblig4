import astropy.stats

n = float(input('Utvalgets størrelse: '))
x = float(input('Antall merkede fra utvalget: '))
p_hat = float(input('Skriv inn KI prosent: '))

p_hat = p_hat / 100
my_hat = float((x / n))

# Calculates normal distribution
norm_dist = float((n * p_hat) * (1 - p_hat))

# Calculates confidence interval
conf_interval = astropy.stats.binom_conf_interval(x, n, p_hat)

diff = round(my_hat - conf_interval[0], 3)

if norm_dist >= 5:
    print(
        'Informasjonen oppfyller kravet for normalfordeling med konfidensintervall:\n',
        conf_interval, '\n', my_hat, ' ± ', diff)
else:
    print('Informasjonen oppfyller ikke kravet for normalfordeling.')

