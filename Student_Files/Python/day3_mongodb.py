from pymongo import MongoClient


def extract_full_name(document):
    if document:
        full_name = document["first_name"] + " " + document["last_name"]

        return full_name


# create a client (localhost:27017 by default)
client = MongoClient()

# grab a reference to the students database
studentsDB = client.studentsDB

# execute a find all (select *) against the students collection
students_cursor = studentsDB.students.find()

# iterate through the returned BSON and print it out
for student in students_cursor:
    # print(document)
    # print(document["first_name"], document["last_name"])
    print(extract_full_name(student))

# grab a reference to the flights database
flightsDB = client.flightsDB

# execute a find all (select *) against the flights collection
flights_cursor = flightsDB.flights.find()

for flight in flights_cursor:
    print(flight["flight_number"], flight["origin"],
          flight["destination"], flight["flight_time"])

client.close()
