import os.path
import csv

def show_all_users():

    if os.path.exists("data/users.csv"):
        with open("data/users.csv", "r") as userscsv:
            data = csv.DictReader(userscsv)
            return list(data)
    else:
        return ">>> users.csv NOT EXISTS."

        
def insert_user(user):
    """        
    Insert data in csv file.
    :params: name, age, salary, email
    :return: if register success return true.
    """    
    fields = ["name", "age", "salary", "email"]
    
    if not os.path.exists("data/users.csv"):
        with open("data/users.csv", "w") as user_csv:
            w = csv.DictWriter(user_csv, fieldnames = fields)
            w.writeheader()

    with open("data/users.csv", "a") as user_csv:
        w = csv.DictWriter(user_csv, fieldnames = fields)
        w.writerow({"name":     user["name"], 
                    "age":      user["age"], 
                    "salary":   user["salary"], 
                    "email":    user["email"]})
        return True
    return False
