def solution(n):
    answer = 0
    
    dp = [0] * 600001
    
    dp[2] = 2
    dp[3] = 3    
    
    if n < 4:
        return dp[n]
    
    for i in range(4,n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    
    answer = dp[n]
    return answer