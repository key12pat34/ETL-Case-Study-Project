#dependencies
import numpy as np
# import datetime as dt
import pandas as pd
import random
import os

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


# #################################################
# # Database Setup
# #################################################

# path
engine = create_engine("postgres://rucnhzitaxpivk:abe8cbc751cf2611667d1c7e508efca9bc96f820f5e75cc62cdd3470809e86b2@ec2-52-22-238-188.compute-1.amazonaws.com:5432/d6m3qgh80itc7j")


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
Quotes = Base.classes.quotes
Author_info = Base.classes.author_info
Tags = Base.classes.tags

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
        f"/api/v1.0/top10tags"
    )

            
@app.route("/api/v1.0/quotes")
def quotes():
    # get total number of quotes scrapped
    # get quote information (text, author name, and tags)
    sel=[quotes.author_name, quotes.text, Tags.tags]
    
    quote_info = session.query(*sel).\
        filter(Quotes._id == Tags._id).all()     

    session.close()


    # text, name, and tags (qry) --> [{Text:text}, {Name:name}, {Tags:tags}]
    quote_list=[]
    for name, text, tags in quote_info:
        info_dict = {}
        info_dict["Text"] = text
        info_dict["Author"] = name
        info_dict["Tags"] = tags
        quote_list.append(info_dict)
    
    quotes_libr = {"total":len(quote_list), "quote":quote_list}


    # Return the JSON representation of your dictionary.
    return (quotes_libr) 

# @app.route("/api/v1.0/top10tags")
# def top10tags():
# #     # get tag name, and count
#     tagunique = []
#     tags = session.query(Tags.tags).all()
#     for tag in tags:
#         tags.type()
#         if tag in tagunique:
#             continue
#         else:
#             tagunique.append(tags)

# #     # list only the top 10
#     # top_ten_tag = session.query(Tags.tags).all()

#     session.close()

#     tags_libr = {"total":len(tagunique), "tags":tagunique}
#     # top10tags = {"total":len(tagunique), "tags":tagunique}
#     # return jsonify(top_ten_tag)
#     return jsonify(tags_libr)

@app.route("/api/v1.0/top10tags")
def top10tags():
    result = []
    tags_result_set = engine.execute('''select tag , count(*) as total from tags
    group by tag
    order by total desc
    limit 10''')
    for row in tags_result_set:
        tag = {}
        tag['tag'] = row.tag
        tag['total'] = row.total
        result.append(tag)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug = True)