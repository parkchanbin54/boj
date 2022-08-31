import sys

def sol():
    input = sys.stdin.readline

    n, m = map(int,input().split())

    A = [list(map(int,input().rstrip())) for _ in range(n)]
    B = [list(map(int,input().rstrip())) for _ in range(n)]

    count = 0

    def check():
        for i in range(n):
            for j in range(m):
                if A[i][j] != B[i][j]:
                    return False
        return True

    def reverse(x,y):
        for i in range(x,x+3):
            for j in range(y,y+3):
                A[i][j] = 1 - A[i][j]

    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B[i][j]:
                reverse(i,j)
                count += 1

    if check():
        print(count)
    else:
        print(-1)




if __name__ == '__main__':
    sol()
