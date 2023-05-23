r, c = map(int, input().split())

row = [0, r]   
column = [0, c]

for _ in range(int(input())): 
    r_or_c, linenumber = map(int, input().split())  
    if r_or_c == 1:             
        row.append(linenumber)
    else :
        column.append(linenumber)

row.sort()     
column.sort()  
subtracted_r = []  
subtracted_c = []  

for i in range(len(row)-1):   
    subtracted_r.append(row[i + 1] - row[i])   
for i in range(len(column) -1):
    subtracted_c.append(column[i+1]- column[i])

print(max(subtracted_r) * max(subtracted_c))