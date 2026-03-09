# For each value of r calculate the population size and plot the data
# r = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]
# Consider the above vector as values of r measured yearly across 17 years. 
# Answer the question What will bee the population growth in year 17?

import matplotlib.pyplot as plt

r_values = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]

x0 = 0.5
population = [x0]

for r in r_values:
    x_next = r * population[-1] * (1 - population[-1])
    population.append(x_next)

years = range(len(population))

plt.figure()
plt.plot(years, population, marker='o')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth Over 17 Years (Logistic Model)")
plt.grid(True)
plt.show()

# 2.4
print("Population each year:")
for i, value in enumerate(population):
    print(f"Year {i}: {value}")

print("\nPopulation in year 17:", population[-1])