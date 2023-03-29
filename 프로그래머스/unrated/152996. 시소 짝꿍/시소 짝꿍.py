from collections import defaultdict

def solution(weights):
    answer = 0
    
    dis = [3/2, 2, 2/3, 4/3, 2/4, 3/4]

    dict = defaultdict(int)
    
    for w in weights:
        dict[w] += 1
    
    keys = list(dict.keys())
    
    for k in keys:
        if dict[k] > 1:
            answer += dict[k] * (dict[k] -1)
        for d in dis:
            answer += dict[k] * dict[k * d]
            
    answer = answer // 2
    
        
    return answer