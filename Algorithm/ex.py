N = int(input())

i = 0
while i != N:

    i+=1
    hap = i
    for j in str(i):
        hap += int(j)

    if hap == N:
      print(i)
      break