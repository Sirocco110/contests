n,x = map(int, input().split())
a = list(map(int, input().split()))

discount = len(a) // 2

total = sum(a) - discount


if x >= total:
    print("Yes")
else:
    print("No")