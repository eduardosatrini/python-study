def show_options():
    print()
    print("=-"*30)
    print("{:^30}".format("Register CSV").upper())
    print("=-"*30)
    print("[ 1 ] Show all users")
    print("[ 2 ] Create user")
    print("[ 3 ] Update users # not implemented")
    print("[ 4 ] Delete user # not implemented")
    print("[ 5 ] Quit")
    print("--"*30)
    print()


def show_headers():
    print("{:^20} {:^3} {:^7} {:^5}".format("name", "age", "salary", "email").title())
    print("--"*30)
