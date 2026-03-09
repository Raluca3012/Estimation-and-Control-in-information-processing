# Make a simulation by using the logistic regression expression = population growth.
# Use a growth factor r=0.9. Make a raport (word doc) that describes the fate
# of the population for r=0.9

import matplotlib.pyplot as plt

r = 0.9           
x0 = 0.5         
iterations = 50   

population = [x0]

for i in range(iterations):
    x_next = r * population[-1] * (1 - population[-1])
    population.append(x_next)

time = range(len(population))


plt.figure()
plt.plot(time, population, marker='o')
plt.xlabel("Time step")
plt.ylabel("Population")
plt.title("Population Growth using Logistic Model (r = 0.9)")
plt.grid(True)
plt.show()

for i, value in enumerate(population):
    print(f"Step {i}: {value}")