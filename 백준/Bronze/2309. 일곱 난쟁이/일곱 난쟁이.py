n = 9
arr = [int(input()) for _ in range(n)]
arr.sort()
 
for i in range(n):
    for j in range(i+1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                print(arr[k])
            exit()
 
print('\n'.join(map(str, arr)))