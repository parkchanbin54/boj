def solution(brown, yellow):
    answer = []
    
    for i in range(brown//2):
        for j in range(i+1):
            if i * j == brown + yellow:
                if (i * 2) + (j * 2) - 4 == brown:
                    return [i, j]      
    
    return answer