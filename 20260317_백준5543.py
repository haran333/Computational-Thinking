price = list(int(input()) for _ in range(5))
print(min(price[0], price[1], price[2]) + min(price[3], price[4]) - 50)