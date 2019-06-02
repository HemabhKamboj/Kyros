from flask import Flask, session, request, render_template, redirect, jsonify, flash
from sqlalchemy import create_engine
import requests
import folium

app = Flask(__name__)


engine = create_engine("postgres://dwtwkhpihgaedb:866d89ea4688710f804d0258d799588a39aa40b738a3e9cbe99795b33e2e0241@ec2-54-225-72-238.compute-1.amazonaws.com:5432/deik5m0otb9kgc")

@app.route("/cardata", methods=["GET"])
def cardata():
    """ Get car data """

    # Check car id was provided
    if not request.args.get("carid"):
        return "you must provide a car id."

    # # Take input and add a wildcard
    # query =request.args.get("carid")

    # # Capitalize all words of input for search
    # # https://docs.python.org/3.7/library/stdtypes.html?highlight=title#str.title
    # query = query.title()

    rows = engine.execute("SELECT * FROM car_data WHERE car_id ={}".format(request.args.get("carid")))
                    #   {"query":request.args.get("carid")})


    return jsonify({'rows': [dict(row) for row in rows]})
    # result = dict(rows)

    # return jsonify(result)                  


@app.route("/createmap", methods=["GET"])
def getmap():
    latitude = request.args.get("lat")
    longitude = request.args.get("long")
    location = [latitude, longitude]
    # results = map_search[0]
    # return jsonify({'result': [dict(result) for result in results]})
    m = folium.Map(location=location, zoom_start=9)
     
    current_location_icon = folium.features.CustomIcon('current.png', icon_size=(20,30))

    folium.Marker(location, popup='<strong>Current Location</strong>',icon = current_location_icon).add_to(m)

    map_search = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=NDMC+delta+EV+chargers+in+delhi&key=AIzaSyCoOv22Ipjh2mNjjpASLlhE47jcMNfWG-Q")
    result = map_search.json()
    result_length = len(result)
    all_results = []
    for i in range(result_length):
        lat = result['results'][i]['geometry']['location']['lat']
        longi = result['results'][i]['geometry']['location']['lng']
        loc1 = [lat, longi]
        all_results.append(loc1)
        folium.Marker(loc1, icon=folium.Icon(color='crimson')).add_to(m)
        


    map_search.json()
    return m._repr_html_()

