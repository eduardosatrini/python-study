def table_price(v, v_increase = 35, v_decrease = 20):
    print("=-"*12)
    print("TABLE PRICE".center(12))
    print("=-"*12)
    print(f"Price analysing: {currency(v)}")
    print(f"Half: {half(v, True)}")
    print(f"Double: {double(v, True)}")
    print(f"Increase {v_increase}%: {increase_percent(v, v_increase, True)}")
    print(f"Decrease {v_decrease}%: {decrease_percent(v, v_decrease, True)}")
    print("--"*12)


def currency(v, currency_type = "R$"):
    return f"{currency_type}{v:.2f}".replace(".", ",")


def half(n, f = False):
    result = n / 2
    return result if f == False else currency(result)


def double(n, f = False):
    result =  n * 2
    return result if f == False else currency(result)


def increase_percent(value, percent, f = False):
    result =  value + (value * percent / 100)
    return result if f == False else currency(result)


def decrease_percent(value, percent, f = False):
    result =  value - (value * percent / 100)
    return result if f == False else currency(result)
