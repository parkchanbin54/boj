import sys

n,c = map(int, input().split())
li = []
li.append(input().split())
li = li[0]
dic = {}
for i in li:
  if i not in dic:
    dic[i] = 1
  else:
    dic[i] += 1
dic = sorted(dic.items(), key=lambda x : -x[1])
for i in range(len(dic)):
    print((dic[i][0]+' ') * dic[i][1], end='')
