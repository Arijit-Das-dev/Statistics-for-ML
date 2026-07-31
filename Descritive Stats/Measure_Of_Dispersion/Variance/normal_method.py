# AVERAGE / MEAN
def mean(data: list) -> float:

    total = 0
    for i in range(0, len(data)):
        total = total + data[i]

    average = total/len(data)
    return average

# VARIANCE
def var(data: list) -> float:

    """
        σ² = Σ(xᵢ - μ)² / N
        
        xᵢ = Each data point
        μ = Average or mean
        N = data size
        σ² = Standard Daviation
    """

    N = len(data)           # LENGTH OF DATASET
    U = mean(data=data)     # AVERAGE OF THE DATASET
    summ = 0

    for i in range(0, len(data)):
        summ = summ + (data[i] - U)**2

    variance = summ/N
    return variance

sales = [120, 980, 150, 760, 210, 1300, 90, 650, 180, 1100]
print(var(data=sales))