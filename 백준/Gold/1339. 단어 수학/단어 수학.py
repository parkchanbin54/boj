import sys

n = int(sys.stdin.readline())

alpha = [] 
alpha_dict = {}
numList = [] 

for i in range(n):
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n): 
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_dict: 
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)
        else:  
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values(): 
    numList.append(val)

numList.sort(reverse=True)

sum = 0
pows = 9
for i in numList: 
    sum += pows * i
    pows -= 1

print(sum)