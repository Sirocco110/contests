t = int(input())
case = [(input()) for _ in range(t)]


for i in case:
    ans = 0
    ans1 = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0

    if i[-1] == "0":
        ans = 4
    elif i[-1] == "9" or i[-1] == "8" or i[-1] == "7":
        ans = 3
    elif i[-1] == "6" or i[-1] == "5" or i[-1] == "4":
        ans = 2
    else:
        ans = 1
    
    if i[-1] == "1" or i[-1] == "2" or i[-1] == "3":
        n = list(set(i))
    else:
        n = list(set(i[:-1]))
    for j in n:
        if j == "0":
            ans4 = 4
            break
        elif j == "9" or j == "8" or j == "7":
            ans3 = 3
        elif j == "6" or j == "5" or j == "4":
            ans2 = 2
        else:
            if ans3 == 3 or ans2 == 2:
                ans1 = 4
            else:
                ans1 = 1
    print(max(ans,ans1,ans2,ans3,ans4))