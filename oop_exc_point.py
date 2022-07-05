# 1
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#
# pt = Point(1, 2)
# try:
#     print(pt.z)
# except AttributeError:
#     print('Атрибут с именем z не существует')

# 2
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


values = input().split()
try:
    pt = Point(int(values[0]), int(values[1]))
except ValueError:
    try:
        pt = Point(float(values[0]), float(values[1]))
    except ValueError:
        pt = Point()
finally:
    print(f'Point: x = {pt._x}, y = {pt._y}')
