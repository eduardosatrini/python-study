def grade(*notes, situation = False):
    """ 
    Calc grade notes and show a situation
    the student's.
    :param 1: grade student with packing
    :param 2: situation student.
    :return: a dictionarie.
    """         
    values["total"] = len(notes)
    values["major"] = max(notes)
    values["minor"] = min(notes)
    values["media"] = sum(notes) / len(notes)

    if situation:
        if values["media"] < 5:
            values["situation"] = "Bad!"
        elif values["media"] >= 5 and values["media"] <= 7:
            values["situation"] = "More or less!"
        else:
            values["situation"] = "Good!"        

    return values
    

result = grade(10, 7, 6, 3, situation = True)

