import copy
tmp = []
ans = []

def back_tracking(sale, n):
    if len(tmp) == n:
        ans.append(copy.deepcopy(tmp))
        return
    
    for s in sale:
        tmp.append(s)
        back_tracking(sale,n)
        tmp.pop()

def solution(users, emoticons):
    sale = [10,20,30,40]
    
    back_tracking(sale,len(emoticons))
    
    answer = [0,0]
    for an in ans:
        pre, mon = 0,0
        for user in users:
            umon = 0
            for i in range(len(an)):
                if an[i] >= user[0]:
                    umon += int(emoticons[i] * (100 - an[i]) / 100)
            if umon >= user[1]:
                pre += 1
            else:
                mon += umon

        if pre > answer[0]:
            answer = [pre,mon]
        elif pre == answer[0] and mon > answer[1]:
            answer = [pre, mon] 
            
    print(answer)
            
            
            
        
    
    
    
    
    return answer