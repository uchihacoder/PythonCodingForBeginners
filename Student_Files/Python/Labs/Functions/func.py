# def repeatit(output, number=5):
#     for i in range(0, number):
#         print(output)


# repeatit(number=10, output="hello")

def secured_access(user_type):

    user = user_type.upper()

    def inner_func():
        print("Inner Function Called!")

    if isinstance(user, str) and user == "ADMIN":
        inner_func()
        return True
    else:
        print("You do not have permission to call the inner function")
        return False


has_access = secured_access("admin")

print(f'has access?  {has_access}')

# secured_access.inner_func()
