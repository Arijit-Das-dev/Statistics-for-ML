# most repeated value -> 

import numpy as np
import statistics as stats

data = [10, 20, 30, 10, 40, 50, 20, 60, 70, 30, 80, 90, 10]

names = [
    "Alice", "Bob", "Charlie", "Alice", "David",
    "Bob", "Eva", "Frank", "Charlie", "Alice"
]

print("Mode : ", stats.mode(data))
print("Mode : ", stats.mode(names))