n = int(input())
a = list(map(int, input().split()))

half = len(a)//2

not_list = []
for i in range(half):
    if a[i] != a[len(a)-1-i]:
        not_list.append(a[i])
        not_list.append(a[len(a)-1-i])

if len(not_list) != 0:
    print(len(set(not_list))-1)
else:
    print(0)

#辺でつなぐ集合が2つ以上だと上のやり方では多く見積もっている
#つながる辺同士の集合が必要
