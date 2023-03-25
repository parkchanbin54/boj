def getgcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a
    
def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    l = len(arrayA)
    
    a = arrayA[0]
    for i in range(1,l):
        a = getgcd(a,arrayA[i])
        
    b = arrayB[0]
    for i in range(1,l):
        b = getgcd(b,arrayB[i])
    
    check = [True, True]
    for i in range(l):
        if arrayA[i] % b == 0:
            check[0] = False
        if arrayB[i] % a == 0:
            check[1] = False
    
    if check[0] and check[1]:
        answer = max(a,b)
    elif check[0]:
        answer = b
    elif check[1]:
        answer = a
    
    return answer