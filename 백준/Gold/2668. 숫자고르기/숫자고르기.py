import sys
import copy

def pick(idx, first, second):
    first.add(idx)
    second.add(nums[idx])

    if nums[idx] in first:
        if first == second:
            answer.update(first)
        return
    return pick(nums[idx],first,second)


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    nums = [0]+[int(input()) for _ in range(n)]

    answer = set()

    for i in range(1,n+1):
        if i not in answer:
            pick(i,set(),set())

    print(len(answer))
    for i in sorted(list(answer)):
        print(i)