s = list(input())

h = (int("".join(s[:2])))

t = (int("".join(s[2:])))

if h <= 12 and h >= 1:
    if t <= 12 and t >= 1:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if t <= 12 and t >= 1:
        print("YYMM")
    else:
        print("NA")