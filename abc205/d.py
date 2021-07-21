n,q = (map(int, input().split()))
a = list(map(int, input().split()))
k = [int(input()) for _ in range(q)]

int_list = list(range(1,a[-1]+1))

diff = list(set(a) ^ set(int_list))

# print(a)
# print(k)
# print(diff)


for i in k:
    if i > len(diff):
        print(a[-1] + i - len(diff))
    else:
        print(diff[i-1])

    
#何故かわからん