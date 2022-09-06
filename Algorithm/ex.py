a, b = map(int, input().split())

c = []
d = 0
for i in range(a+1):
	if not a%i:
		c.append(i)
for j in range(b+1):
	if not b%i and b//i in c:
		d = i
print(d)
