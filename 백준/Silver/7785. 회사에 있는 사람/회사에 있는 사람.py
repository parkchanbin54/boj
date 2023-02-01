import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    people = {}
    for _ in range(n):
        name, tmp = input().split()
        people[name] = tmp

    people = sorted(people.items(), key = lambda item: item[0], reverse = True)

    for p in people:
        if p[1] == 'enter':
            print(p[0])
