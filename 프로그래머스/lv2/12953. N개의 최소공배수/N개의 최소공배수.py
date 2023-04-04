
def gcd(a,b):
    while b > 0:
        a,b = b, a %b
    return a

def lcd(a,b):
    return a * b/ gcd(a,b)

def solution(arr):
    answer = 0
    answer = arr[0]
    for a in arr[1:]:
        answer = lcd(answer, a)
        
    return answer

