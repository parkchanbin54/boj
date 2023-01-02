from itertools import permutations
import sys

if __name__ == '__main__':                                            
    input = sys.stdin.readline                                        
                                                                      
    n = int(input())                                                  
                                                                      
    nums = list(map(int,input().split()))                             
                                                                      
    per = permutations(nums)                                          
    ans = 0                                                           
                                                                      
    for p in per:                                                     
        s = 0                                                         
        for j in range(len(p) - 1):                                   
            s += abs(p[j]-p[j+1])                                     
        if s > ans:                                                   
            ans = s                                                   
                                                                      
    print(ans)                                                        
                                                                      