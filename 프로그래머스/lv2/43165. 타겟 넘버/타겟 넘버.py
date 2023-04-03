from itertools import product

def solution(numbers, target):
    answer = 0
    pro = list(product([1,-1], repeat = len(numbers)))
    
    for p in pro:
        sum = 0
        for i,j in enumerate(p):
            sum += numbers[i] * j
        
        if sum == target:
            answer += 1
            
    return answer