import sys
import copy
sys.setrecursionlimit(10 ** 9)

def solution(queue1, queue2):
    answer = -1
    total = sum(queue1) + sum(queue2)
    t = total//2
    
    left = 0
    right = len(queue1)
    cur = sum(queue1)
    
    queue1 += queue2
    
    cnt = 0
    while right < len(queue1):
        if cur == t:
            answer = cnt
            break
        
        elif cur < t:
            cur += queue1[right]
            right +=1
    
        else:   
            cur -= queue1[left]
            left += 1
        
        cnt += 1
    
        
    
        
    return answer