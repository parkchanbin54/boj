def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    dr = ['d','l','r','u']
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    
    start = (x,y)
    
    stack = []
    stack.append((x,y, ''))
    
    while stack:
        x,y,path = stack.pop()
        if len(path) == k and (x,y) == (r,c):
            answer = path
            break
        remain, sp = k-len(path), abs(r-x) + abs(c-y)
        if remain < sp or remain % 2 != sp % 2:
            continue
            
        if x > 1:
            stack.append((x-1,y,path+"u"))
        if y < m:
            stack.append((x,y+1,path+"r"))
        if y > 1:
            stack.append((x,y-1,path+"l"))
        if x < n:
            stack.append((x+1,y,path+"d"))
            
    return answer