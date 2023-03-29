


def solution(storey):
    answer = 0
    
    nums = [0]+list(map(int,str(storey)))
     
    for i in range(len(nums)-1,0,-1):
        if nums[i] > 5 or (nums[i] == 5 and nums[i-1] > 4):
            nums[i-1] += 1
            answer += 10 - nums[i]
            nums[i] = 0
    print(nums)
    answer += sum(nums)
        
    return answer