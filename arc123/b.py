n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort()
b.sort()
c.sort()

ans = 0

j = 0
k = 0

# print(a)
# print(b)
# print(c)


for i in a:
    while i >= b[j]:
        j += 1
        if j == n:
            break
    if j >= n:
        break
    
    while b[j] >= c[k]:
        k += 1
        if k == n:
            break
    if k >= n:
        break
    ans += 1
    j += 1
    k += 1

    if j >= n or k >= n:
        break

# print(i,b[j],c[k])
print(ans)


