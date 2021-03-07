print("MARKET STORE")
print("=-"*12)

total_price = cheapest_product = most_expensive = 0
product_cheapest_name = product_expensive_name = ""
c = 1
while True:
    product_name = str(input("Product name: ")).strip()
    price = float(input("Price: R$"))

    if c == 1:
        cheapest_product = price
        most_expensive = price
        product_expensive_name = product_name
        product_cheapest_name = product_name
    c += 1
    
    total_price += price

    if price > most_expensive:
        most_expensive = price
        product_expensive_name = product_name
    if price < cheapest_product:
        cheapest_product = price
        product_cheapest_name = product_name
        
    keep = str(input("Continue [Y/N]? ")).strip().upper()
    if keep != "Y":
        break
print(f"Total: R${total_price:.2f}")
print(f"Most expensive: {product_expensive_name} R${most_expensive:.2f}")
print(f"Most cheapest: {product_cheapest_name} R${cheapest_product:.2f}")
