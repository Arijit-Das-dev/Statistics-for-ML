# Mean using statistics library
# Sample mean
# Population mean

import statistics as stats

# Population mean
population = [12, 13, 14, 15, 16]

population_mean = stats.mean(population)
print(population_mean)


# Sample mean
sample = [12, 13, 14]

sample_mean = stats.mean(sample)
print(sample_mean)