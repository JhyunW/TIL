x, y, w, h = map(int, input().split())

x_move = 0
y_move = 0


if w-x >= x:
    x_move = x
else:
    x_move = w-x

if h-y >= y:
    y_move = y
else:
    y_move = h-y

if x_move >= y_move:
    print(y_move)
else:
    print(x_move)