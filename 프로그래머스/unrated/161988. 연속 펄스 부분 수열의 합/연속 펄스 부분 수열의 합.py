def getsum(arr):
    m = 0
    i = 0
    while i < len(arr):
        if arr[i] > 0:
            tmp = arr[i]
            m = max(m, tmp)
            for j in range(i+1,len(arr)):
                tmp += arr[j]
                if tmp < 0:
                    break
                i = j
                m = max(m, tmp)
        i += 1 
    return m

def solution(sequence):
    a = []
    b = []
    for i, s in enumerate(sequence):
        if i % 2 == 0:
            a.append(-s)
            b.append(s)
        else:
            b.append(-s)
            a.append(s)
    
    asum = getsum(a)
    bsum = getsum(b)
        
    answer = max(asum,bsum)
    return answer