a1,a2,a3 = map(int,input().split())

diff1_2 = a2-a1
diff2_3 = a3-a2
did = diff2_3 - diff1_2
ans = 0

if did > 0:
    ans = did // 2 + (did%2)*2
elif did < 0:
    ans = -did

print(ans)