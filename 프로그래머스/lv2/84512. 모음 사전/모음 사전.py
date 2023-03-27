tmp = []
cnt = 0
def back_tracking(word,words):
    global cnt
    if ''.join(tmp) == word:
        answer = cnt
        return cnt
        
    elif len(tmp) == 5:
        return 0
    
    for w in words:
        tmp.append(w)
        cnt += 1
        re = back_tracking(word,words) 
        if re != 0 and re != None:
            return re
        tmp.pop()
    


def solution(word):
    answer = 0
    
    words = ['A','E','I','O','U']
    
    answer = back_tracking(word,words)
    return answer