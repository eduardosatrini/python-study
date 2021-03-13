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


def background(txt):
    # background blue
    if ":bg_blue:" in txt:
        value = txt.replace(":bg_blue:", "\033[44m")
        if ":bg_blue_:":
            return value.replace(":bg_blue_:", "\033[m")
    return txt

    # background green
    if ":bg_green:" in txt:
        value = txt.replace(":bg_green:", "\033[42m")
        if ":bg_green_:":
            return value.replace(":bg_green_:", "\033[m")
    return txt
    
    # background red
    if ":bg_red:" in txt:
        value = txt.replace(":bg_red:", "\033[41m")
        if ":bg_red_:":
            return value.replace(":bg_red_:", "\033[m")
    return txt

    # background white
    if ":bg_white:" in txt:
        value = txt.replace(":bg_white:", "\033[40m")
        if ":bg_white_:":
            return value.replace(":bg_white_:", "\033[m")
    return txt
