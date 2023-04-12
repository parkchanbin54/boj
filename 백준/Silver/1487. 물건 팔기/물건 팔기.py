n = int(input())
c_list = []
d_list = []
for i in range(n):
	cost,deli = map(int,input().split())
	c_list.append(cost)
	d_list.append(deli)

c_set = sorted(set(c_list))

max_m = 0 
ans = 0
for i in c_set:
	money = 0
	for j in range(n):
		if i <= c_list[j] and i > d_list[j]:
			money += i-d_list[j]
	
	if max_m < money:
		max_m = money
		ans = i
	
print(ans)