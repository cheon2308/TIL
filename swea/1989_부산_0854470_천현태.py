T = int(input())

for i in range(1, T+1):
    s = input()
    s = s.lower()
    r = s[::-1]
    r = r.lower()
    if s == r:
        print ('#%d %d' % (i, 1) )
    else:
        print ('#%d %d' % (i, 0) )
