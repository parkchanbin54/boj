import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    books = list(map(int,input().split()))

    mem = [-1]

    for book in books:
        if mem[-1] < book:
            mem.append(book)

        else:
            left = 0
            right = len(mem)

            while left < right:
                mid = (left + right)//2

                if mem[mid] < book:
                    left = mid + 1
                else:
                    right = mid

            mem[right] = book

    print(n - len(mem) + 1)
