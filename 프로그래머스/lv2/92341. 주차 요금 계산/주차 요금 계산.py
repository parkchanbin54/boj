from datetime import datetime
from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    l = list(records[0].split())
    print(l)
    
    dict = {}
    ans = defaultdict(int)
    
    for record in records:
        r = list(record.split())
        if r[1] not in dict:
            dict[r[1]] = r[0]
        else:
            ans[r[1]] += (datetime.strptime(r[0],'%H:%M') - datetime.strptime(dict[r[1]],'%H:%M')).seconds//60
            del dict[r[1]]
    
    for d in dict:
        ans[d] += ((datetime.strptime('23:59', '%H:%M') - datetime.strptime(dict[d], '%H:%M')).seconds//60)
        
    result = defaultdict(int)
    for a in ans:
        if ans[a] < fees[0]:
            result[a] += fees[1]
        else:
            result[a] += (fees[1] + math.ceil((ans[a] - fees[0]) / fees[2]) * fees[3])
    
    key = list(result.keys())
    
    key.sort()
    
    for k in key:
        answer.append(result[k])
        
    return answer