n = int(input())
c = list(map(int, input().split()))

c.sort()

total = 1
check = 0

for i in range(len(c)):
    if (c[i] - i) <= 0:
        check = 1
        break

    total *= (c[i] - i) % 1000000007
    total = total % 1000000007

if check == 1:
    print(0)
else:
    print(total % 1000000007)
