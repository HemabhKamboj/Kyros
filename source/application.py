from flask import Flask, session, request, render_template, redirect, jsonify, flash
from sqlalchemy import create_engine

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
