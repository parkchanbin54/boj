
def bs(s, e, t):
    global lower

    if s > e:
        return 

    m = (s + e) // 2

    if LIS[m] > t:
        lower = m
        bs(s , m - 1, t)
    else:
        bs(m + 1, e, t)


N = int(input())
L_ARR = list(map(int, input().split()))
R_ARR = list(map(int, input().split()))

# 1
O_ARR = [0 for n in range(N + 1)]
for i, v in enumerate(R_ARR):
    O_ARR[v] = i + 1

# 2
LIS = []
TRA = []
lower = 0

for l in L_ARR:
    o = O_ARR[l]
    if len(LIS) == 0 or LIS[-1] < o:
        TRA.append(len(LIS))
        LIS.append(o)
    else:
        bs(0, len(LIS) - 1, o)
        LIS[lower] = o
        TRA.append(lower)

# 3
res = []
chk = max(TRA)
for v in TRA[::-1]:
    N -= 1
    if chk == v:
        res.append(L_ARR[N])
        chk -= 1

# 4
print(len(res))
print(' '.join(map(str, sorted(res))))