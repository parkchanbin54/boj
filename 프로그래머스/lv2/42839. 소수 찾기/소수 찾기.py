tmp = []
ind = []
ans = set()
def isprime(x):
    for i in range(2,x//2+1):
        if x % i == 0:
            return False
    return True

def back_tracking(arr):
    if len(tmp) != 0:
        t = int(''.join(tmp))
        if isprime(t) and t != 0 and t != 1:
            ans.add(t)

    for i in range(len(arr)):
        if i not in ind:
            tmp.append(arr[i])
            ind.append(i)
            back_tracking(arr)
            tmp.pop()
            ind.pop()
    
def solution(numbers):
    answer = 0
    
    nums = list(numbers)
    
    back_tracking(nums)
    answer = len(ans)
    
    return answer
