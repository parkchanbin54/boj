from collections import deque
import sys

sys.setrecursionlimit(10**9)
dp = []
numMap = {
    0 : (3,1),
    1 : (0,0),
    2 : (0,1),
    3 : (0,2),
    4 : (1,0),
    5 : (1,1),
    6 : (1,2),
    7 : (2,0),
    8 : (2,1),
    9 : (2,2),
}

#y,x 순
distance = {
    (0,0) : 1,
    (0,1) : 2,
    (1,0) : 2,
    (1,1) : 3,
    (2,0) : 4,
    (0,2) : 4,
    (2,1) : 5,
    (1,2) : 5,
    (2,2) : 6,
    (3,0) : 6,
    (3,1) : 7,
}
dp = [[[-1] * 100001 for _ in range(10)] for _ in range(10)]

def getDistance(a,b):
    a = numMap[a]
    b = numMap[b]
    return (abs(a[0]-b[0]), abs(a[1]-b[1]))

def dfs(left,right,idx,result):
    if idx == len(result):
        return 0
    
    if dp[left][right][idx] != -1:
        return dp[left][right][idx]
    
    next = int(result[idx])
    if next == left or next == right:
        dp[left][right][idx] = dfs(left, right, idx + 1, result) + 1
        return dp[left][right][idx]
    
    else:
        dp[left][right][idx] = min(distance[getDistance(left,next)] + dfs(next,right,idx + 1, result), distance[getDistance(next,right)] + dfs(left,next,idx+1,result))

    return dp[left][right][idx]
    
    
    
def solution(numbers):
    answer = 0
    
    answer = dfs(4,6,0,numbers)
    return answer