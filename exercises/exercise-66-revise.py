print("="*12)
print("{:^12}".format("BANK"))
print("="*12)

value = int(input("Value: R$"))
total = value

banknote = 50
banknote_total = 0

while True:
    if total >= banknote:
        total -= banknote
        banknote_total += 1
    else:
        if banknote_total > 0:
            print(f"Banknotes {banknote_total} - R${banknote}")
            
        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1

        banknote_total = 0
            
        if total == 0:
            break
print("Check back often!")
