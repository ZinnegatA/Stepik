def input_int_numbers():
    try:
        return tuple(int(i) for i in input().split())
    except ValueError:
        raise TypeError('все числа должны быть целыми')


while True:
    try:
        print(*input_int_numbers())
    except TypeError:
        continue
    else:
        break
