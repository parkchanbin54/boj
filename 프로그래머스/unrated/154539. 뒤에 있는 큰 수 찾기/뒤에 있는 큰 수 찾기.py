def solution(numbers):
    tmp = [numbers[-1]]
    stack = []
    answer = [-1 for i in range(len(numbers))]
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    
    return answer