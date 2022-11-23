import sys

if __name__ == '__main__':
    prime = [True] * 1000001
    prime[0],prime[1] = False,False

    for i in range(2,1000):
        if prime[i]:
            for j in range(i,1000000//i + 1):
                prime[i*j] = False


    while True:
        n = int(input())
        if n == 0:
            break

        for i in range(n):
            if i == n-1:
                print("Goldbach's conjecture is wrong.")
            if prime[i] and prime[n-i]:
                print('{0} = {1} + {2}'.format(n,i,n-i))
                break


