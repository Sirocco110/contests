s = input()

dp = [[0]*(len(s)+1) for i in range(9)]
moji = "chokudai"

for i in range(8):
    num = 0
    if i == 0:
        for j in range(len(s)):
            if moji[i] == s[j]:
                num += 1
            dp[i+1][j+1] = num

    else:
        for j in range(len(s)):
            if moji[i] == s[j] and dp[i][j] > 0:
                num = dp[i+1][j] + dp[i][j]%1000000007
            dp[i+1][j+1] = num

print(dp[8][len(s)]%1000000007)
