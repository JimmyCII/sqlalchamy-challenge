#Import dependencies
import numpy as np
import pandas as pd
import datetime as dt


# Import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
# session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
        # Find the most recent date in the data set.
    most_recent_date = session.query(func.max(Measurement.date)).first()

    # Calculate the date one year from the last date in data set.
    last_date = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d')
    one_year_ago = last_date - dt.timedelta(days=365)


    # Perform a query to retrieve the data and precipitation scores
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    session.close()
    # Create dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}

    return jsonify(precipitation_dict)
    

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
    # List the stations and observation counts in descending order.
    stations_data = session.query(Station.station).all()
    session.close()
    stations = list(np.ravel(stations_data))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    # Design a query to get the previous 12 months of temperature observation (TOBS) data.
    most_active_station_id = 'USC00519281'  # Replace this with the ID of the most active station if needed
    # Find the most recent date in the data set.
    most_recent_date = session.query(func.max(Measurement.date)).first()
    session = Session(engine)
    # Calculate the date one year from the last date in data set.
    last_date = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d')
    one_year_ago = last_date - dt.timedelta(days=365)


    tobs_data = session.query(Measurement.date, Measurement.tobs)\
                       .filter(Measurement.station == most_active_station_id)\
                       .filter(Measurement.date >= one_year_ago)\
                       .all()
    
    tobs_list = {date: tobs for date, tobs in tobs_data}
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def get_temps_start(start):
    session = Session(engine)
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs))\
                .filter(Measurement.date >= start_date).all()
    session = Session(engine)
    temps = list(np.ravel(results))
    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")
def get_temps_start_end(start, end):
    session = Session(engine)
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs))\
                .filter(Measurement.date >= start_date)\
                .filter(Measurement.date <= end_date).all()
    session = Session(engine)
    temps = list(np.ravel(results))
    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)

# Close Session
# session.close()