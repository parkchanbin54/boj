import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        blocks = [int(input()) for _ in range(n)]

        mem = [-1]

        for block in blocks:
            if mem[-1] < block:
                mem.append(block)

            else:
                left = 0
                right = len(mem)

                while left < right:
                    mid = (left + right) // 2

                    if mem[mid] < block:
                        left = mid + 1
                    else:
                        right = mid

                mem[right] = block

        print(len(mem)-1)