import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    energies = list(map(int,input().split()))
    answer = 0
    def back_tracking(x):
        global answer

        if len(energies) == 2:
            answer = max(answer , x)
            return

        for i in range(1, len(energies) - 1):
            target = energies[i-1] * energies[i+1]

            v = energies.pop(i)
            back_tracking(x+target)
            energies.insert(i,v)

    back_tracking(0)
    print(answer)
