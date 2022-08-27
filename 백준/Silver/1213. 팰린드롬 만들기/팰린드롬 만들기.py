import sys
word = sys.stdin.readline().strip()    
alphas = [0 for _ in range(27)]        
odds = 0                               
oddIndex = -1                           
for letters in word:
    alphas[ord(letters)-65] += 1
for i in range(len(alphas)):
    if alphas[i] % 2 == 1:              
        odds += 1
        oddIndex = i    
        if odds == 2:                   
            print("I'm Sorry Hansoo")
            exit()
alphas[oddIndex] -= 1                  
for i in range(len(alphas)):            
    if alphas[i] % 2 != 1:
        for _ in range(alphas[i]//2):
            print(chr(i+65), end="")
if oddIndex != -1:
    print(chr(oddIndex+65), end="")     
for i in range(len(alphas)-1, -1, -1): 
    if alphas[i] % 2 != 1:
        for _ in range(alphas[i]//2):
            print(chr(i+65), end="")