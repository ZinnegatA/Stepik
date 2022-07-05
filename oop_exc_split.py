ls = input().split()
try:
    res = int(ls[0]) + int(ls[1])
except ValueError:
    try:
        res = float(ls[0]) + float(ls[1])
    except ValueError:
        res = ls[0] + ls[1]
finally:
    print(res)
