students = {}

while True:
    print("=" * 40)
    print(" (A) Add\n (D) Delete\n (L) List\n (Q) Quit")
    print("=" * 40)

    selection = input("Please enter a command >  ").upper()

    if selection == "A":
        print("Adding")
        add_sid = input("Please enter identifier>  ")
        add_student_full_name = input("Please enter full name>  ")
        add_student_age = input("Please enter age>  ")
        add_student_address = input("Please enter address>  ")

        if (add_sid and add_student_full_name and add_student_age and add_student_address):
            students[add_sid] = [add_student_full_name,
                                 add_student_age, add_student_address]

        else:
            print(
                f"You did not enter all of the information.  You entered\n sid: {add_sid}\n full name: {add_student_full_name}\n age: {add_student_age}\n address: {add_student_address}")

    elif selection == "D":
        print("Deleting")
        delete_sid = input("Please enter identifier>  ")
        del students[delete_sid]
    elif selection == "L":
        print("Listing")
        for sid in students.keys():
            student = students[sid]
            print(f"{sid}, {student[0]}, {student[1]}, {student[2]}")
    elif selection == "Q":
        break
    else:
        print(f"Invalid command: {selection}.  Please enter a valid command.")
