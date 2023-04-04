def solution(s):
    answer = 0
    s = list(s)
    l = len(s) 
    dp = [[0] * l  for _ in range(l)]
    
    for i in range(l):
        for j in range(l - i):
            e = j + i
            if j == e:
                dp[j][e] = 1
            else:
                if s[j] == s[e]:
                    if j + 1 == e: dp[j][e] = 1
                    elif dp[j+1][e-1] == 1:
                            dp[j][e] = 1
     
    for i,d in enumerate(dp):
        for j,p in enumerate(d):
            if p:
                answer = max(answer, j+1 - i)
            
    
    
    return answer