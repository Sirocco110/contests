n = int(input())

s = input()

for i in range(len(s)):
    if s[i] == "1":
        if i%2 == 1:
            print("Aoki")
        else:
            print("Takahashi")
        
        break