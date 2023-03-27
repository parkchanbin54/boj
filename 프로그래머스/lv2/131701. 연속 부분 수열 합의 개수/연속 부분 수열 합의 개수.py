
def solution(elements):
    answer = 0
    
    n = len(elements)
    elements += elements
    
    asum = [[0] * (n) for _ in range(n)]
    ans = set()
    for i in range(n):
        tmp = 0
        for j in range(i,i+n):
            tmp += elements[j]
            asum[i][j-i] = tmp
            ans.add(tmp)

    answer = len(ans)
            
        
    
    return answer