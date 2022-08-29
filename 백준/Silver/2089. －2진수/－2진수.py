import sys

N = int(sys.stdin.readline())

power = [0, 0, 1]
max_table = [0, 0, 1]
min_table = [0, 0, 1]
while (N < 0 and power[-1] > N) or (N > 0 and power[-1] < N):
    if N <= max_table[-1] and N >= min_table[-1]:
        break

    power.append(power[-1] * (-2))
    if power[-1] > 0:
        max_table.append(max_table[-2] + power[-1])
        min_table.append(min_table[-1] + power[-1])
    else:
        max_table.append(max_table[-1] + power[-1])
        min_table.append(min_table[-2] + power[-1])

res = ''
now = N
for idx in range(len(power)-1, 1, -1):
    if max_table[idx] >= now and min_table[idx] <= now:
        res += '1'
        now -= power[idx]
    else:
        res += '0'

sys.stdout.write(res)