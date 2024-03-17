products_of_3 = {}
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            products_of_3[product] = (i, j)

print(max(products_of_3), max(products_of_3.values()))  # 906609  (924 * 962)
