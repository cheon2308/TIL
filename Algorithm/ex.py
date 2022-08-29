num = [i for i in range(1,10001)]

gen = []

for i in range(len(num)):
    number = int(i)
    for j in str(i):
        number += int(j)
    gen.append(number)

for k in set(gen):
    num.remove(k)

for l in num:
    print(l)