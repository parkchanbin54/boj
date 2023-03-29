from collections import Counter
import copy

def isprime(arr):
    arr[1] = 1
    for i in range(2,len(arr)//2+1):
        for j in range(i+i, len(arr), i):
            arr[j] += 1
        
    return arr

def solution(e, starts):
    answer = []
    numset = [2 for i in range(e+1)]
    numset = isprime(numset)
    dict = {}
    seqdict = {}
#     for s in starts:
#         answer.append(numset[s:].index(max(numset[s:])) + s)
    
    cnt = Counter(starts)
    
    seq = copy.deepcopy(starts)
    seq.sort()
    
    m = max(numset[seq[0]:])
    dict[seq[0]] = (numset[seq[0]:].index(m) + seq[0])
    seqdict[seq[0]] = m
    
    for i in range(1,len(seq)):
        if seqdict[seq[i-1]] == max(numset[seq[i-1]:seq[i]]):
            if seq[i] != e:
                m = max(numset[seq[i]:])
                dict[seq[i]] = (numset[seq[i]:].index(m) + seq[i])
                seqdict[seq[i]] = m
            else:
                dict[seq[i]] = e
        else:
            dict[seq[i]] = dict[seq[i-1]]
            seqdict[seq[i]] = seqdict[seq[i-1]]
    
    
    for s in starts:
        answer.append(dict[s])
    
            
    
    
    
    return answer