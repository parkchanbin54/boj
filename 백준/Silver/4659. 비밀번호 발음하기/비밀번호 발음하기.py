import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    while True:
        tmp = input().rstrip()

        if tmp == "end":
            break

        tmp = list(tmp)
        alpha = ['a','e','i','o','u']
        check = False
        flag = True

        prev = []
        queue = deque()
        queue_tmp = deque()
        for t in tmp:
            if t in alpha:
                queue_tmp.append(1)
                check = True
            else:
                queue_tmp.append(0)
            if len(queue) != 0:
                if queue[-1] == t:
                    if t != 'e' and t != 'o':
                        flag = False
                        break
            queue.append(t)
            if len(queue) == 3:
                if sum(queue_tmp) == 3 or sum(queue_tmp) == 0:
                    flag = False
                    break
                else:
                    queue.popleft()
                    queue_tmp.popleft()
        if flag and check:
            print("<"+''.join(tmp)+"> is acceptable.")
        else:
            print("<"+''.join(tmp)+"> is not acceptable.")