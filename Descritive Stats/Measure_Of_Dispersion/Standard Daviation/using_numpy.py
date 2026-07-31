# STANDARD DAVIATION

import numpy as np

data = [0, 2, 4, 5, 6, 8, 10]

"""
σ² = √ Σ(xᵢ - μ)² / N

xᵢ = Each data point
μ = Average or mean
N = data size
σ² = Standard Daviation

"""
data = np.array(
    data
)

mean = np.mean(data)
std = np.std(data)

print("Average : ", mean)
print("Standard daviation : ", round(std, 2))

# 1SD -> showing 68% of the data boundary 

negative_value = int(mean - std)
positive_value =  int(mean + std)

print("Start Range (-ve) : ", positive_value)
print("End Range (+ve) : ", negative_value)

print("1 SD -> ")
inside = data[(data >= negative_value) & (data <= positive_value)]
print("68% of the data lies between :  ", inside)