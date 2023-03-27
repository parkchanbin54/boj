def solution(cards):
    answer = 0
    cards = [-1] + cards
    n = len(cards)
    
    ans = []   
    picked = [False] * n
    for i in range(1,n):
        set1 = set()
        if not picked[i]:
            set1.add(i)
            prev = i
            while True:
                picked[prev] = True
                if cards[prev] in set1:
                    ans.append(set1)
                    break
                else:
                    prev = cards[prev]
                    set1.add(prev)

    ans.sort(key = len, reverse = True)
    
    if len(ans) >= 2:    
        answer = len(ans[0]) * len(ans[1])
    
    
                 
        
    
    return answer