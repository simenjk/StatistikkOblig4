import random
import numpy as np
import matplotlib.pyplot as plt

roll_num = int(input('Hvor mange kast per omgang?: '))
turn_num = int(input('Hvor mange omganger?: '))

turn_count = np.ma.zeros(turn_num)
avg_turn_count = np.ma.zeros(turn_num)
total_avg = 0

for turn in range(turn_num):
    for roll in range(roll_num):
        # Generates random number from 1 to 6. (Dice)
        random_num = random.randint(1, 6)
        # Adds random number to turn_count array
        turn_count[turn] += random_num
    # Calculates average dice roll for every turn
    avg_turn_count[turn] = turn_count[turn] / roll_num
    # Adds average dice turn to total
    total_avg += avg_turn_count[turn]

# Divide total by number of turns
total_avg /= turn_num

# Calculates standard deviation
standard_deviation = np.std(avg_turn_count)

# Output for average roll every turn
# print(avg_turn_count)

print('Gjennomsnitt total: %s \nStandardavvik: %s' % (round(total_avg, 4), round(standard_deviation, 4)))

x = np.arange(1, 30 + 1)
if len(avg_turn_count) >= 30:
    plt.bar(x, avg_turn_count[:30])
    plt.show()
else:
    print('Omganger må være >= 30 for å plotte graf.')
