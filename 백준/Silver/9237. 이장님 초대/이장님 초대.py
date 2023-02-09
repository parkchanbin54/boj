import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    tree = list(map(int,input().split()))

    tree.sort(reverse = True)
    days = len(tree)

    for i in range(n):
        tree[i] += i

    print(max(tree) + 2)
