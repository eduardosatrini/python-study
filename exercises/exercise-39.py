price = float(input("Purchase price: R$"))

print("""
====================
PAYMENT METHODS
[1] In cash
[2] Debit card
[3] 2x Credit card
[4] 3x or more install
====================
""")

option = int(input("Wich option: "))
price_final = discount = installment_price = fees = 0
if option == 1:
    discount = price * 10 / 100
    price_final = price - discount
elif option == 2:
    discount = price * 5 / 100
    price_final = price - discount
elif option == 3:
    installment_price = price / 2
    price_final = price   
elif option == 4:
    installment = int(input("Installment:"))
    fees = price * 20 / 100
    price_final = price + fees
    installment_price = price_final / installment
else:
    print("Invalid number!")
print("="*20)
print(f"Total purchase amount: R${price_final:.2f} | Discount: R${discount:.2f}")
print(f"Price installment: R${installment_price:.2f} | Fees: R${fees:.2f}")
