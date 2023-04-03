import copy
tmp = ['ICN']
ans = []
def dfs(x,tickets,used,cnt):
    if cnt == len(tickets):
        ans.append(copy.deepcopy(tmp))
        return 
    
    for i,ticket in enumerate(tickets):
        if tickets[i][0] == x and not used[i]:
            used[i] = True
            tmp.append(tickets[i][1])
            dfs(tickets[i][1], tickets, used, cnt+ 1)
            used[i] = False
            tmp.pop()
            
def solution(tickets):
    answer = []
    l = set()
    for a,b in tickets:
        l.add(a)
        l.add(b)
    used = [False] * len(tickets)
    
    dfs("ICN",tickets,used,0)
        
    ans.sort()
    answer = ans[0]
    
        
        
    return answer