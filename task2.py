x, y, z = map(int, input().split())
price_pencil = 3
price_pen = price_pencil + 2
price_marker = price_pen + 7
total = x * price_pencil + y * price_pen + z * price_marker
print(total)