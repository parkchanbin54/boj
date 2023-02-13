import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    a,b = map(int,input().split())

    dow = int(input())

    tops = [int(input()) for _ in range(n)]
    tops.sort(reverse = True)


    low = dow //a

    for top in tops:
        if low <= (dow + top)//(a+b):
            low = (dow + top)//(a+b)
            a += b
            dow += top
        else:
            break

    print(dow//a)