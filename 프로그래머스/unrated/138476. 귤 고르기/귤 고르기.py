from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    cnt = defaultdict(int)
    
    for t in tangerine:
        cnt[t] += 1
        
    result = []
    for c in cnt:
        result.append((c,cnt[c]))
    
    result.sort(key = lambda x : -x[1])
    
    tmp = 0
    
    for r in result:
        if tmp >= k:
            break
        tmp += r[1]
        answer += 1
        
    return answer