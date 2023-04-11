def solution(k, d):
    answer = 0
    arr = [(i*i) for i in range(0,d+1,k)]
    limit = d * d
    
    for i in range(len(arr)):
        left, right= 0, len(arr)-1
        while left < right:
            mid = (left + right)//2
            if arr[mid] + arr[i] < limit:
                left = mid + 1
            else:        
                right = mid
                
        answer += left + 1
        
        if arr[left] + arr[i] > limit:
            answer -= 1

    
    return answer