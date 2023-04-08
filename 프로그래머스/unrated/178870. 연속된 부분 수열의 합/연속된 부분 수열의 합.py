def solution(sequence, k):
    answer = []
    n = len(sequence)
    end = 0
    s = 0
    
    ans = []
    for i in range(n):
        
        while s < k and end < n:
            s += sequence[end]
            end += 1
        
        if s == k:
            ans.append([i,end-1, end-1-i])
        
        s -= sequence[i]
    
    ans.sort(key = lambda x : x[2])
    
    answer = ans[0][:2]
            
    return answer