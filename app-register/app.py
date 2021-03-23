from lib.crud import users
from lib.interface import view
from time import sleep

while True:
    view.show_options()
    option = int(input("Option: "))

    if option == 1:
        users_data = users.show_all_users()
        if users_data:
            view.show_headers()
            for u in users_data:
                print(f"{u['name']:^20} {u['age']:^3} {u['salary']:^7} {u['email']}")
        sleep(1)
    elif option == 2:
        data = dict()
        data["name"] = str(input(">>> Name: "))
        data["age"] = int(input(">>> Age: "))
        data["salary"] = float(input(">>> Salary: "))
        data["email"] = str(input(">>> Email: "))

        r = users.insert_user(data) 
        if r:
            sleep(0.5)
            print("\n >>>>> Registered with success! \n")
            sleep(0.5)
        else:
            print("Failed register.")
            break 
    if option >= 5:
        print("Exit program.. ", end = "")
        for i in "bye!":
            print(i, end = "", flush = True)
            sleep(0.5)
        break        
