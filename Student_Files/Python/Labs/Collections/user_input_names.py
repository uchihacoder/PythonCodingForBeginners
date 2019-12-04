from Student_Service import Student_Service

student_srvc = Student_Service()


def convert_sid(sid):
    if sid:
        return int(sid)

# sd_input = input("Please enter a student identifier>  ")


while True:
    print("=" * 40)
    print(" (A) Add\n (D) Delete\n (S) Search\n (L) List\n (Q) Quit")
    print("=" * 40)

    selection = input("Please enter a command >  ").upper()

    if selection == "A":
        sid = convert_sid(input("Please enter identifier>  "))

        full_name = input("Please enter full name>  ")
        age = input("Please enter age>  ")

        if not age.isdigit():
            continue

        age = int(age)

        address = input("Please enter address>  ")

        student_srvc.add_student(sid, full_name, age, address)

    elif selection == "D":
        sid = convert_sid(input("Please enter identifier>  "))

        student_srvc.delete_student(sid)

    elif selection == "S":
        sid = convert_sid(input("Please enter identifier>  "))

        student_srvc.search_for_a_student(sid)

    elif selection == "L":
        student_srvc.list_students()

    elif selection == "Q":
        break

    else:
        print(f"Invalid command: {selection}.  Please enter a valid command.")
