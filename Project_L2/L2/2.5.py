# Make a series of experiments in which the population number starts from 
# a) 0.1 b) 0.5 c) 1.0 d) 2
# Make a report in which you note the observations for r = 4

import matplotlib.pyplot as plt

R = 4
initial_populations = [0.1, 0.5, 1.0, 2.0]
generations = 20


fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle(f"Population Growth Experiments (R = {R})", fontsize=16)

axes = axes.flatten()

for i, P0 in enumerate(initial_populations):
    population_history = [P0]
    current_P = P0
    
    for _ in range(generations):
        try:
            current_P = R * current_P * (1 - current_P)
            population_history.append(current_P)
        except OverflowError:
            population_history.append(float('-inf'))
            break 
            
        
    ax = axes[i]
    ax.plot(range(len(population_history)), population_history, marker='o', color='teal')
    titles = ["a) P0 = 0.1", "b) P0 = 0.5", "c) P0 = 1.0", "d) P0 = 2.0"]
    ax.set_title(titles[i])
    ax.set_xlabel("Generations")
    ax.set_ylabel("Population Fraction")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.axhline(0, color='red', linestyle='--', linewidth=1) 

plt.tight_layout(rect=[0, 0.03, 1, 0.95])


image_filename = 'Screenshot_5'
plt.savefig(image_filename, dpi=150)
plt.close() 


