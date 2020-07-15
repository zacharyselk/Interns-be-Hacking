from flask import jsonify, render_template, request, redirect, url_for
from server import app
import requests
from cloudant.client import Cloudant

"""
Business Logic for the make assignment screen
"""
@app.route("/make_assignment", methods=['POST'])
def make_assignment():
    return render_template('make_assignment.html')

"""
Business Logic for the home screen
"""
@app.route("/do_assignment")
def do_assignment():
    return render_template('do_assignment.html')


"""
Business Logic for submitting the make assignment form
This is triggered by url_for() when form is submitted
after completion, should send user back to the make assignment screen
and give an indicator of success (green check mark?)
"""
@app.route("/add_assignment", methods=['POST'])
def add_assignment():
    URL = "93be668d-82a1-4b5e-aeaa-70dcd895b019-bluemix.cloudant.com/learnathome_users"
    form_data = dict(request.form)
    data = {}
    data["assignment_name"] = form_data["title"]
    data["assignment_text"] = form_data["comment"]
    data["assignment_duedate"] = form_data["Enddate"]
    data["assignment_skill"] = form_data["skill"]
    # r = requests.post(URL, data=data, auth=('IMkPio4zsgC7zmYmcmp6tL1ueCqbT65cawkXG4bS9JOS', ))
    # print(r)
    #print(request.form)
    client = Cloudant.iam("93be668d-82a1-4b5e-aeaa-70dcd895b019-bluemix",
                          "IMkPio4zsgC7zmYmcmp6tL1ueCqbT65cawkXG4bS9JOS",
                          connect=True)
    mydatabase = client['learnathome_users']
    mydatabase.create_document(data)
    return render_template('make_assignment.html')
    #return redirect(url_for('make_assignment'))