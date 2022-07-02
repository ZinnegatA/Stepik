# 1
lst_in = input().split()


def check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


print(sum(list(map(int, filter(check, lst_in)))))

# 2
lst_in = input().split()


def f(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x


lst_out = list(map(f, lst_in))
