from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    me = Counter(topping)
    bro = defaultdict(int)
    for i in range(len(topping)):
        bro[topping[i]] += 1
        me[topping[i]] -= 1
        
        if me[topping[i]] == 0:
            del me[topping[i]]
        
        if len(bro) == len(me):
            answer += 1
        elif len(bro) > len(me):
            break
            
        
            
        
    return answer