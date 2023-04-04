import math
from itertools import permutations
minMap = {
    "diamond" : 0,
    "iron" : 1,
    "stone" : 2,
}

def solution(picks, minerals):
    answer = 0

    minerals_set = []
    count = math.ceil(len(minerals) / 5)
    tmp = []
    for i, pick in enumerate(picks):
        if len(tmp) + pick > count:
            for _ in range(count - len(tmp)):
                tmp.append(i)
        else:
            for _ in range(pick):
                tmp.append(i)
    graph = [[1,1,1],[5,1,1],[25,5,1]]
    
    for i in range(0,len(minerals), 5):
        m = [[]]
        total = 0
        for j in range(5):
            if i+j >= len(minerals):
                break
            m[0].append(minMap[minerals[i+j]])
            total += graph[2][minMap[minerals[i+j]]]
        
        m.append([len(m[0]),total])
        minerals_set.append(m)
    if count > sum(picks):
        minerals_set.pop()
    minerals_set.sort(key = lambda x : -x[1][1])
    print(minerals_set)
    idx = 0
    for t in tmp:
        for i in range(5):
            if len(minerals_set[idx][0]) <= i:
                break
            answer += graph[t][minerals_set[idx][0][i]]
        idx += 1
    
    return answer