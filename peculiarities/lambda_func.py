# Using lambdas

def product_numbers(x, y, z): # normal function
    return x * y * z

    
print(product_numbers(3, 6, 2))


products = lambda x, y, z: x * y * z # same function now with lambda
print(products(3, 8, 2))

