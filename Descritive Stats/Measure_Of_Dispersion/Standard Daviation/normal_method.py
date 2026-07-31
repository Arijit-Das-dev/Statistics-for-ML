import math

# GETTING AVERAGE
def get_average(data: list) -> float:

    total = 0
    for i in range(0, len(data)):
        total += data[i]

    avg = total/len(data)
    return avg

# GETTING STANDARD DAVIATION
def standard_daviation(data: list) -> float:
    """
        σ² = √ Σ(xᵢ - μ)² / N

        xᵢ = Each data point
        μ = Average or mean
        N = data size
        σ² = Standard Daviation
    """
    average = get_average(data=data)

    summ = 0
    N = 0
    for i in range(0, len(data)):

        N = N + 1
        summ = summ + (data[i]-average)**2

    variance = summ/N
    std = math.sqrt(variance)

    return std

sales = [120, 980, 150, 760, 210, 1300, 90, 650, 180, 1100]

std = standard_daviation(data=sales)
print(std)