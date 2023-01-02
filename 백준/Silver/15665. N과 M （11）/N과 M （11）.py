import sys

if __name__ == '__main__':                                  
    input = sys.stdin.readline                              
                                                            
    N, M = map(int,input().split())                         
                                                            
    nums = list(map(int,input().split()))                   
    nums.sort()                                             
    temp = []                                               
    count = 0                                               
    v = 0                                                   
    def back_tracking():                                    
        if len(temp) == M:                                  
            print(*temp)                                    
            return                                          
        prev = 0                                            
        for i in range(len(nums)):                          
            if prev != nums[i]:                             
                temp.append(nums[i])                        
                prev = nums[i]                              
                back_tracking()                             
                temp.pop()                                  
                                                            
    back_tracking()                                         
                                                            
                                                            