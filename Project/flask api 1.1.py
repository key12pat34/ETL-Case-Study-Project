#dependencies
import numpy as np
import datetime as dt
import pandas as pd
import random

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


# #################################################
# # Database Setup
# #################################################

# path
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f'Quote scraper endpoints<br>'
        f"/api/v1.0/quotes<br/>"
        f"/api/v1.0/authors<br/>"
        f"/api/v1.0/authors/<author name><br>"
        f"/api/v1.0/tags<br>"
        f"/api/v1.0/tags/<tag><br>"
        f"/api/v1.0/top10tags<br>"
    )

            




@app.route("/api/v1.0/quotes<br/>")
def quotes():
    # get total number of quotes scrapped
    quote_count = session.query()
    # get quote information (text, author name, and tags)






#   { total: <total number quotes scraped >,
#     quotes : [{ text: <quote text >,
#                 author name: <author name >,
#                 tags: []},
# 	            ...]
#    }


@app.route("/api/v1.0/authors<br/>")
def authors():
    # get total number of authors

    # get author detail(name, description, date of birth, total quote count by author, list of all the quotes)




#     {total: <total number of authors>,
#      details:[{ name : <author name >,
#             	  description : <author description>,
#             	  born : <date of birth etc. >,
#             	  count : <total number of quotes by this author >,
#             	  quotes : [{ text: <quote text>,
#                     		  tags: []}, 
#                 ...]
#             	},
#      	...]
#      }


@app.route("/api/v1.0/authors/<author name><br>")
def author_name():
    # get author information (name, description, date of birth, number of quotes, list quotes)


#     {name: <Author name>,
#      description: <author description>,
#      born: <date of birth etc>
#      number_of_quotes :  <total quotes by the author>
#      quotes : [{ text: <quote text>,
#     			   tags: []},
#                ...]
#      }


@app.route("/api/v1.0/tags<br>")
def tags():
    # get total tag count
    tag_count = session.query(tags.tag).count()
    #  get tag details (tag name, number of quotes, quote)
    tag_detail = session.query(tags.tag, )

    session.close()



#     { count: <total tags>,
# 	    details:[{ name: < tag>,
#         		   number_of_quotes :  <total quotes this tag appears in >,
#         		   quotes : [{ text: <quote text>, tags: []}, ... ]},
#                  ...]
#      }


@app.route("/api/v1.0/tags/<tag><br>")
def tag_name():
    # get tag name, tage count, and quotes


#     { tag : <tag name>,
# 	    count : <number of quotes this tag appears in >,
# 	    quotes : [{ quote : <quote text >, tags : []}, ...	]
#      }


@app.route("/api/v1.0/top10tags<br>")
def top10tags():
    # get tag name, and count
    # list only the top 10
    top_ten_tag = session.query(tags.tag).count()

    # 	[{ tag: < tag name > ,
    #      quote count: < number of quotes this tag appears in >}, ...]




if __name__ == '__main__':
    app.run(debug = True)

##################################
### DELETE EVERY THING BELOW######
##################################


# def precipitation():
#     #getting the last date in the datebase
#     last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
#     last_date = last_date[0]


#     # date 1 year last_data
#     one_year_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)
#     one_year_ago = one_year_ago.strftime("%Y-%m-%d")

#     # query for date and prcp
#     perciptation_results = session.query(Measurement.date, Measurement.prcp).\
#         filter(Measurement.date >= one_year_ago).all()
   
#     session.close()

#     # date and prcp (qry) --> [{date:prcp}]
#     date_prcp_list=[]
#     for date,prcp in perciptation_results:
#         prcp_dict = {}
#         prcp_dict[date] = prcp
#         date_prcp_list.append(prcp_dict)
    
#     # Return the JSON representation of your dictionary.
#     return jsonify(date_prcp_list)


# @app.route("/api/v1.0/stations")
# def stations():    
#     # Return a JSON list of stations from the dataset.
#     station_list = session.query(Station.station).all()

#     #combining multiple lists into one
#     station_dict = list(np.ravel(station_list))
#     session.close()
    
#     return jsonify(stations = station_dict)


# @app.route("/api/v1.0/tobs")
# def tobs():
#     # Query the dates and temperature observations of the most active station for the last year of data.
#     # Return a JSON list of temperature observations (TOBS) for the previous year.

#     #getting the last date in the datebase
#     last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
#     last_date = last_date[0]

    
#     # date 1 year last_data
#     one_year_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)
#     one_year_ago = one_year_ago.strftime("%Y-%m-%d")

#     # most active station
#     active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
#         group_by(Measurement.station).\
#         order_by(func.count(Measurement.station).desc()).all()

#     most_active_station = active_stations[0][0]

#     #temperature query
#     temp_results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
#         filter(Measurement.station == most_active_station).\
#         filter(Measurement.date >= one_year_ago).all()

#     session.close()

#     # station, date, and tobs (qry) --> [{date: date, station:station, temp:temp}]
#     temp_list=[]
#     for station, date, tobs in temp_results:
#         temp_dict = {}
#         temp_dict['station'] = station
#         temp_dict['date'] = date
#         temp_dict['temp'] = tobs
#         temp_list.append(temp_dict)

#     return jsonify(temp_list)




# @app.route("/api/v1.0/<start>")
# def start(start):
#     # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#     # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    
#     # Random Start date
#     start_date = session.query(Measurement.date).order_by(func.random()).first()    
#     start_date = start_date[0]


#     sel=[Measurement.date,
#         func.min(Measurement.tobs),
#         func.max(Measurement.tobs),
#         func.avg(Measurement.tobs),]

#     min_max_avg_qry = session.query(*sel).\
#         filter(Measurement.date >= start_date).all()
    
#     session.close()

#     # date, Tmin, Tmax, Tavg(qry) --> [{Tavg:tavg, Tmax:tmax, Tmin:tmin, date:date}]
#     min_max_avg_list=[]
#     for date, Tmin, Tmax, Tavg in min_max_avg_qry:
#         min_max_avg_dict = {}
#         min_max_avg_dict['date'] = date
#         min_max_avg_dict['Tmin'] = Tmin
#         min_max_avg_dict['Tmax'] = Tmax
#         min_max_avg_dict['Tavg'] = Tavg
#         min_max_avg_list.append(min_max_avg_dict)

#     return jsonify(min_max_avg_list)

# @app.route("/api/v1.0/<start>/<end>")
# def start_end(start,end):
#     # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#     # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    
#     # Random Start date
#     start_date = session.query(Measurement.date).order_by(func.random()).first()    
#     start_date = start_date[0]

#     #getting the last date in the datebase
#     last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
#     last_date = last_date[0]

#     # Calculating the date 10 days before last_date
#     ten_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=10)
#     ten_ago = ten_ago.strftime("%Y-%m-%d")



#     sel=[Measurement.date,
#         func.min(Measurement.tobs),
#         func.max(Measurement.tobs),
#         func.avg(Measurement.tobs),]

#     min_max_avg_qry = session.query(*sel).\
#         filter(Measurement.date >= start_date).\
#         filter(Measurement.date <= ten_ago).all()

#     session.close()

#     # date, Tmin, Tmax, Tavg(qry) --> [{Tavg:tavg, Tmax:tmax, Tmin:tmin, date:date}]
#     min_max_avg_list=[]
#     for date, Tmin, Tmax, Tavg in min_max_avg_qry:
#         min_max_avg_dict = {}
#         min_max_avg_dict[' start date'] = date
#         min_max_avg_dict['Tmin'] = Tmin
#         min_max_avg_dict['Tmax'] = Tmax
#         min_max_avg_dict['Tavg'] = Tavg
#         min_max_avg_list.append(min_max_avg_dict)

#     return jsonify(min_max_avg_list)




# if __name__ == '__main__':
#     app.run()