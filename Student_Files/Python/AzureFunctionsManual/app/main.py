from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
flights_db = client.flightsDB


@app.route("/")
def welcome_to_flights():
    return "Welcome to Flights!"


@app.route("/flights", methods=["POST"])
def add_flight():

    if not request.json or not "flight_number" in request.json:
        abort(400)

    new_flight = {
        "flight_number": request.json["flight_number"],
        "origin": request.json["origin"],
        "destination": request.json["destination"]
    }

    result = flights_db.flights.insert(new_flight)

    # return f"Added new record with _id: {result}"

    return jsonify({"_id": f"{str(result)}", "message": "Created a new record!"})


@app.route("/flights/<flight_number>", methods=["PUT"])
def update_flight(flight_number):

    update_flight = {
        "flight_number": flight_number,
        "origin": request.json["origin"],
        "destination": request.json["destination"]
    }

    # result = flights_db.flights.update(update_flight)
    result = flights_db.flights.update({"flight_number": flight_number}, "$set": {"flight_number"})

    return jsonify({"_id": f"{str(result)}", "message": "Updated a record!"})


@app.route("/flights/<flight_number>", methods=["DELETE"])
def delete_flight(flight_number):

    result = flights_db.flights.remove({"flight_number": flight_number})

    return jsonify(result)


@app.route("/flights/<flight_number>", methods=["GET"])
def output_flight(flight_number):

    flight = flights_db.flights.find_one({"flight_number": flight_number})

    flight.pop("_id")

    return jsonify(flight)


@app.route("/flights", methods=["GET"])
def output_flights():

    flights = flights_db.flights.find()

    flights_collection = []

    for document in flights:
        # strip off the _id from each document in the collection from MongoDB
        document.pop("_id")
        flights_collection.append(document)

    return jsonify(flights_collection)


if __name__ == "__main__":
    app.run()
