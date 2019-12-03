class Student_Service:

    def __init__(self):
        self.students = {}

    def add_student(self, sid, full_name, age, address):
        if (sid and full_name and age and address):
            self.students[sid] = [full_name, age, address]
            print(f"Student Added!")

        else:
            print(
                f"You did not enter all of the information.  You entered\n sid: {sid}\n full name: {full_name}\n age: {age}\n address: {address}")

    def delete_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            print("Student Deleted!")
        else:
            print(f"Student not found.  You entered: {sid}")

    def search_for_a_student(self, sid):
        if sid in self.students:
            print("Student found!")
            print(f"{self.students[sid]}")
        else:
            print(f"Student not found.  You entered: {sid}")

    def list_students(self):
        for sid in self.students.keys():
            student = self.students[sid]
            print(f"{sid}, {student[0]}, {student[1]}, {student[2]}")
