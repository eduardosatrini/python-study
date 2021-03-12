# Calc factorial with docstring

def factorial(value, show = False):
    """
    -> Calc Factorial.
    :param value: Number for factorial.
    :param show: Optional param wich show sequences.
    :return: Result.
    """
    f = 1
    for v in range(value, 0, -1):
        f *= v
        if show:
            if v > 1:
                print(f"{v} x ", end = "")
            else:
                print(f"{v} = ", end = "")
    return f

print(f"!{factorial(6, True)}")
#help(factorial)
