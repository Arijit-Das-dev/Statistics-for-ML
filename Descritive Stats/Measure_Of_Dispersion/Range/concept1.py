"""
Use case of RANGE :

- We use range to know the difference between max and min value [max - min]
"""

temparature = [22, 22, 25, 34, 43, 21, 45]

max_temp = max(temparature)
min_temp = min(temparature)

print("Maximum temparature : ",max_temp)
print("Minimum temparature : ", min_temp)

# difference between max and min temp

difference = max_temp - min_temp
print("\nDifference between max temparature and min temparature : ", difference, "\n")

# now identifying the difference between all temp with max temp

for i in range(0, len(temparature)):

    if temparature[i] == max_temp:
        continue
    print(f"Day {i+1} : {temparature[i]}")
    diff = max_temp - temparature[i]
    print(f"Differnce between Day {i+1} {temparature[i]} with Day {temparature.index(max_temp)+1} {max_temp} : ", diff)