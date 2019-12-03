from Student_Service import Student_Service

student_srvc = Student_Service()

# students = {}

"""
def add_student(sid, full_name, age, address):
    if (add_sid and add_student_full_name and add_student_age and add_student_address):
        students[add_sid] = [add_student_full_name,
                             add_student_age, add_student_address]
        print(f"Student Added!")

    else:
        print(
            f"You did not enter all of the information.  You entered\n sid: {add_sid}\n full name: {add_student_full_name}\n age: {add_student_age}\n address: {add_student_address}")


def delete_student(sid):
    if delete_sid in students:
        del students[delete_sid]
        print("Student Deleted!")
    else:
        print(f"Student not found.  You entered: {search_sid}")


def search_for_a_student(sid):
    if search_sid in students:
        print("Student found!")
        print(f"{students[search_sid]}")
    else:
        print(f"Student not found.  You entered: {search_sid}")


def list_students():
    for sid in students.keys():
        student = students[sid]
        print(f"{sid}, {student[0]}, {student[1]}, {student[2]}")
"""

while True:
    print("=" * 40)
    print(" (A) Add\n (D) Delete\n (S) Search\n (L) List\n (Q) Quit")
    print("=" * 40)

    selection = input("Please enter a command >  ").upper()

    if selection == "A":
        sid = input("Please enter identifier>  ")

        if not sid.isdigit():
            continue

        sid = int(sid)

        full_name = input("Please enter full name>  ")
        age = input("Please enter age>  ")

        if not age.isdigit():
            continue

        age = int(age)

        address = input("Please enter address>  ")

        student_srvc.add_student(sid, full_name, age, address)

    elif selection == "D":
        delete_sid = input("Please enter identifier>  ")

        student_srvc.delete_student(delete_sid)

    elif selection == "S":
        search_sid = input("Please enter identifier>  ")

        student_srvc.search_for_a_student(search_sid)

    elif selection == "L":
        student_srvc.list_students()

    elif selection == "Q":
        break

    else:
        print(f"Invalid command: {selection}.  Please enter a valid command.")
