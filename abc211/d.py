n,m = map(int,input().split())
route = [[0]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    route[a-1][b-1] = 1
    route[b-1][a-1] = 1

print(route)