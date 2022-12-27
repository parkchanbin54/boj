def solution(want, number, discount):
    answer = 0
    
    
    for i in range(len(discount)-9):
        tmp = discount[i:i+10]
        tmp_dict = {}
        flag = True
        
        for w in want:
            tmp_dict[w] = 0
            
        for t in tmp:
            if t in tmp_dict:
                tmp_dict[t] += 1
                
        for k in range(len(number)):
            if number[k] > tmp_dict[want[k]]:
                flag = False
                break
        
        if flag:
            answer += 1
    
    return answer