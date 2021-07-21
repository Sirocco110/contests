n,a,x,y = map(int, input().split())

p = n-a

if p > 0:
    print((a*x)+(p*y))
else:
    print(n*x)