def solution(n, times):
    answer = 0
    
    left = 0
    right = 1e18
    
    while left < right:
        mid = (left +  right) // 2
        total = 0
        for t in times:
            total += mid // t
        
        if total < n:
            left = mid + 1 
        else:
            right = mid 
    answer = right
    return answer