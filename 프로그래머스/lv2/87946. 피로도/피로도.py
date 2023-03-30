ans = 0

def dfs(dungeons, tmp, indexes):
    global ans
    for i in range(len(dungeons)):
        if tmp[-1] >= dungeons[i][0] and i not in indexes:
            tmp.append(tmp[-1] - dungeons[i][1])
            indexes.append(i) 
            dfs(dungeons, tmp, indexes)
            tmp.pop()
            indexes.pop()
            
        if i == len(dungeons) - 1:
            ans = max(ans, len(tmp) - 1)
            
    

def solution(k, dungeons):
    answer = -1
    global ans
    dungeons.sort(reverse = True)
    
    tmp = [k]
    indexes = []
    
    dfs(dungeons,tmp,indexes)
    
    answer = ans
    return answer