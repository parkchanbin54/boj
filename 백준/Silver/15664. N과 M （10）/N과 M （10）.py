from itertools import permutations
import sys

                                                               
                                                               
if __name__ == '__main__':                                     
    input = sys.stdin.readline                                 
                                                               
    N, M = map(int,input().split())                            
                                                               
    nums = list(map(int,input().split()))                      
                                                               
    nums.sort()                                                
                                                               
    ans = []                                                   
                                                               
    per = permutations(nums, M)                                
                                                               
    for p in per:                                              
        tmp = []                                               
        for i in range(len(p)):                                
            tmp.append(p[i])                                   
        tmp.sort()                                             
        if tmp not in ans:                                     
            ans.append(tmp)                                    
                                                               
    for a in ans:                                              
        for k in a:                                            
            print(k, end=" ")                                  
        print()                                                
                                                                                                 
                                                             