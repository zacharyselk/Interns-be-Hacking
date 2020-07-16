from flask import jsonify, render_template, request, redirect, url_for
from server import app
import mimetypes, io, os
import pprint


"""
Business Logic for the make assignment screen
"""
@app.route("/make_assignment", methods=['POST'])
def make_assignment():
    return render_template('make_assignment.html')


"""
Business Logic for the make assignment screen
"""
@app.route("/login", methods=['POST'])
def login():
    if request.form["userType"] == "Student":
        return redirect(url_for('child_list'))
    else:
        return redirect(url_for('parent_list'))


"""
Business Logic for the do assignment screen
"""
@app.route("/do_assignment", methods=['POST'])
def do_assignment():
    print("In Do Assignment")
    print(request.form)
    id = request.form["id"]
    print(id)
    client = app.config["CLOUDANT"]
    mydatabase = client['learnathome_users']
    document = mydatabase[id]
    if document['_attachments']:
        path = os.path.join(app.config['TEMP_FOLDER'], "temporary.png")
        print(path)
        f = open(path, "wb")
        attachment = document.get_attachment("Attachment1", write_to=f, attachment_type="binary")
        f.close()
        print(document)
    return render_template('do_assignment.html', d=document, att_img=path)

"""
Business Logic for the submit assignment screen
"""
@app.route("/submit_assignment", methods=['POST'])
def submit_assignment():
    client = app.config["CLOUDANT"]
    mydatabase = client['learnathome_users']
    id = request.form["id"]
    print(request.form)
    uploaded_files = request.files.getlist("fileselect[]")
    att_filename = uploaded_files[0].filename
    uploaded_files[0].save(att_filename)
    print(uploaded_files)
    print(att_filename)
    if request.form["chk-box-completed"] == "on":
        mydoc = mydatabase[id]
        mydoc["assignment_status"] = "complete ✅"
        mydoc.save()
        with open(att_filename, "rb") as f:
            content_type = mimetypes.MimeTypes().guess_type('test-img.jpg')[0]
            main_type, sub_type = content_type.split('/', 1)
            msg = f.read()
            mydoc.put_attachment("SUBMISSION1", content_type, msg)
    os.remove(att_filename)
    return redirect(url_for('child_list'))


"""
Business Logic for the parent list screen
"""
@app.route("/parent_list")
def parent_list():
    print("In Parent List")
    client = app.config["CLOUDANT"]
    mydatabase = client['learnathome_users']
    documents = [document for document in mydatabase]
    #return str(pprint.pformat(documents))
    documents = sorted(documents, key=lambda i: i["assignment_duedate"])
    return render_template('parent_list.html', data=documents)

"""
Business Logic for the child list screen
"""
@app.route("/child_list")
def child_list():
    print("In Child List")
    client = app.config["CLOUDANT"]
    mydatabase = client['learnathome_users']
    documents = [document for document in mydatabase]
    #return str(pprint.pformat(documents))
    documents = sorted(documents, key=lambda i: i["assignment_duedate"])
    return render_template('child_list.html', data=documents)


"""
Business Logic for submitting the make assignment form
This is triggered by url_for() when form is submitted
after completion, should send user back to the make assignment screen
and give an indicator of success (green check mark?)
"""
@app.route("/add_assignment", methods=['POST'])
def add_assignment():
    form_data = dict(request.form)
    print(form_data)
    uploaded_files = request.files.getlist("fileselect[]")
    att_filename = uploaded_files[0].filename
    uploaded_files[0].save(att_filename)
    print(uploaded_files)
    print(att_filename)
    data = {}
    data["assignment_name"] = form_data["title"]
    data["assignment_text"] = form_data["comment"]
    data["assignment_duedate"] = form_data["Enddate"]
    data["assignment_skill"] = form_data["skill"]
    data["assignment_status"] = "incomplete ❌"
    data["assignment_link"] = form_data["skill"]
    # r = requests.post(URL, data=data, auth=('IMkPio4zsgC7zmYmcmp6tL1ueCqbT65cawkXG4bS9JOS', ))
    # print(r)
    #print(request.form)
    # client = Cloudant.iam("93be668d-82a1-4b5e-aeaa-70dcd895b019-bluemix",
    #                       "IMkPio4zsgC7zmYmcmp6tL1ueCqbT65cawkXG4bS9JOS",
    #                       connect=True)
    client = app.config["CLOUDANT"]
    mydatabase = client['learnathome_users']
    document = mydatabase.create_document(data)
    with open(att_filename, "rb") as f:
        content_type = mimetypes.MimeTypes().guess_type('test-img.jpg')[0]
        main_type, sub_type = content_type.split('/', 1)
        msg = f.read()
        document.put_attachment("Attachment1", content_type, msg)
    os.remove(att_filename)
    #return render_template('make_assignment.html')
    #return redirect(url_for('make_assignment'))
    return redirect(url_for('parent_list'))