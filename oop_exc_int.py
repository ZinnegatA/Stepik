lst_in = input().split()


def check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


print(sum(list(map(int, filter(check, lst_in)))))
