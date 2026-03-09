# Modify the value of the weight for state B to a value of 0.5
# Plot the evolution of the population for 15 steps based on sequence S.
# Does the population survive after step 15? 

import random
import matplotlib.pyplot as plt

transitions = {
    'A': [('B',0.4), ('C',0.6)],
    'B': [('A',0.5), ('B',0.5)],
    'C': [('A',0.2), ('B',0.2), ('C',0.6)]
}
weights = {
    'A':1.5,
    'B':0.5,
    'C':3.3
}
steps = 15
state = 'A'
S = [state]

for i in range(steps-1):
    r = random.random()
    cumulative = 0
    for next_state, prob in transitions[state]:
        cumulative += prob
        if r <= cumulative:
            state = next_state
            break
    S.append(state)

print("Sequence S:", S)

population = [0.5]

for s in S:
    r = weights[s]
    x_next = r * population[-1] * (1 - population[-1])
    population.append(x_next)

print("\nPopulation values:")
for i,val in enumerate(population):
    print(f"Step {i}: {val}")

time = range(len(population))

plt.figure(figsize=(10,6))
plt.plot(time, population, marker='o')
plt.xlabel("Step")
plt.ylabel("Population")
plt.title("Population Evolution with Modified Weight B = 0.5")
plt.grid(True)
plt.show()