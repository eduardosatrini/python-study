# COLORS

def colore(txt):
    # blue
    if ":blue:" in txt:
        value = txt.replace(":blue:", "\033[34m")
        if ":blue_:" in value:
            return value.replace(":blue_:", "\033[m")
    # green
    if ":green:" in txt:
        value = txt.replace(":green:", "\033[32m")
        if ":green_:" in value:
            return value.replace(":green_:", "\033[m")
    # red
    if ":red:" in txt:
        value = txt.replace(":red:", "\033[31m")
        if ":red_" in value:
            return value.replace(":red_:", "\033[m")
    # bolder        
    if ":b:" in txt:
        value = txt.replace(":b:", "\033[1m")
        if ":b_:" in value:
            return value.replace(":b_:", "\033[m")
    # underline
    if ":u:" in txt:
        value = txt.replace(":u:", "\033[4m")
        if ":u_:" in txt:
            return value.replace(":u_:", "\033[m")
    # negative
    if ":n:" in txt:
        value = txt.replace(":n:", "\033[7m")
        if ":n_:" in txt:
            return value.replace(":n_:", "\033[m")
    return txt
