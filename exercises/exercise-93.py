def show(msg):
    print("="*len(msg))
    print(f"{msg}")
    print("="*len(msg))


msg = str(input("Message: "))
show(msg)
