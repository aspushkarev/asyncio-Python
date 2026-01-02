# Плохой способ
squares = []
for num in range(1, 1000000):
    squares.append(num ** 2)
print(type(squares))

# Хороший способ
squares = (num ** 2 for num in range(1, 1000000))
print(type(squares))