N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]
sum = 0
for i in range(N-1):
    if minVal > cities[i]:
        minVal = cities[i]
    sum += (minVal * roads[i])
    
print(sum)