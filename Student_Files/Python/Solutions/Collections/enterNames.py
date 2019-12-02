# Solutions/Collections/enterNames.py
#

students = { 1: [ "Steve Rogers", 95, "555 Lamar Boulevard"],
             2: [ "Clint Barton", 35, "222 State Street"],
             3: [ "Bruce Banner", 40, "1234 Avenue E"],
             4: [ "Tony Stark",   42, "1000 Broad Street"]}

while True:
    for sid in students.keys():
        student = students[sid]
        print( "{:>2},{:>15}, {:>3}, {:<20}".format( sid, student[0], student[1], student[2]))
    print()
    sid_s = input("enter student id or Q to quit or S to search>")
    if (sid_s.upper() == "Q" or sid_s.upper() == "S"):
        break
    sid   = 0
    if (sid_s.isdigit()):
        sid = int(sid_s)
    name  = input("enter name>")
    age_s = input("enter age>")
    age   = 0
    if (age_s.isdigit()):
        age = int(age_s)
    addr  = input("enter address>")
    student = [ name, age, addr]
    students[sid] = student
    print("-"*60)
if (sid_s == "S"):
    sid_s = input("enter student id to lookup>")
    if (sid_s.isdigit()):
        sid = int(sid_s)
    student = students[sid]
    print( "FOUND: {:>2},{:>15}, {:>3}, {:<20}".format( sid, student[0], student[1], student[2]))
