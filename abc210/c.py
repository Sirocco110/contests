n,k = map(int, input().split())
c = list(map(int,input().split()))

cont = n-k+1

candy_list = {}

for i in c:
    candy_list[i] = 0

tmp = 0
for i in range(k):
    if candy_list[c[i]] == 0:
        tmp += 1
    candy_list[c[i]] += 1
max_num = tmp
for i in range(n-k):
    if candy_list[c[i]] == 1:
        tmp -= 1
    candy_list[c[i]] -= 1
    if candy_list[c[i+k]] == 0:
        tmp += 1
    candy_list[c[i+k]] += 1



    max_num = max(max_num,tmp)

print(max_num)