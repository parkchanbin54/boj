import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m=map(int,input().split())

taller=[set() for _ in range(n)]
shorter=[set() for _ in range(n)]

e=[[] for _ in range(n)] 
e_inv=[[] for _ in range(n)] 

for _ in range(m):
  a ,b=map(int,input().split()) 
  e[a-1].append(b-1) 
  e_inv[b-1].append(a-1) 
  
v=[0 for i in range(n)] 
v_inv=[0 for i in range(n)] 

def find_taller(i): 
  if v[i]: return taller[i]
  v[i]=1
  for j in e[i]: 
    taller[i].add(j)
    taller[i]|=find_taller(j)
  return taller[i]
  
def find_shorter(i):
  if v_inv[i]: return shorter[i]
  v_inv[i]=1
  
  for j in e_inv[i]:
    shorter[i].add(j)
    shorter[i]|=find_shorter(j)
    
  return shorter[i]
  
c=0
for i in range(n):
  find_taller(i)
  find_shorter(i)
  if len(taller[i])+len(shorter[i])==n-1: c+=1
print(c)