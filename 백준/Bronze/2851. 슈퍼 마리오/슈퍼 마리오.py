ans,score = 0,0
for i in range(10):
    score+=int(input())
    if 100-ans >= abs(100-score): 
        ans = score
print(ans)