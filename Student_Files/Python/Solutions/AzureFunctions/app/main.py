from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Flights!'

@app.route('/flight/<flightno>/')
def outputFlight(flightno):
    client = MongoClient()
    db = client.flightDB
    cursor = db.flight.find({'flightno':flightno})
    for document in cursor:
        print('flightno='+str(document['flightno'])+
            ',orig='+str(document['orig'])+
            ',dest='+str(document['dest']))
        orig = str(document['orig'])
        dest = str(document['dest'])
        return render_template('outputFlight.html', flightno=flightno, orig=orig, dest=dest)

if __name__ == '__main__':
    app.run();