import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    prime = [False, False, True] + [True] * 1299707

    for i in range(2, 1299710):
        if prime[i]:
            for j in range(i+i, 1299710, i):
                prime[j] = False

    k = int(input())

    for _ in range(k):
        n = int(input())

        if prime[n]:
            print(0)
        else:
            left = n
            right = n

            count = 1

            while True:
                left -= 1
                if prime[left]:
                    break
                count += 1

            while True:
                right += 1
                if prime[right]:
                    break
                count += 1

            print(count+1)