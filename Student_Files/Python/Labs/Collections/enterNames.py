students = {1: ["Steve Rogers", 95, "555 Lamar Boulevard"],
            2: ["Clint Barton", 35, "222 State Street"],
            3: ["Bruce Banner", 40, "1234 Avenue E"],
            4: ["Tony Stark",   42, "1000 Broad Street"]}

for sid in students.keys():
    student = students[sid]
    print(f"{sid}, {student[0]}, {student[1]}, {student[2]}")
