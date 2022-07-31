import sys
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True
def sol():
    input = sys.stdin.readline
    n = int(input())

    result = 0

    for i in range(n , 1000001):
        if i == 1:
            continue
        if str(i) == str(i)[::-1]:
            if isPrime(i):
                result = i
                break

    if result == 0:
        result = 1003001

    print(result)




if __name__ == '__main__':
    sol()
