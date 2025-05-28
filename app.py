from flask import Flask, render_template, request
from models.queries import Query
from models.setObject import SetObject

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("pages/dashboard.html")

@app.route("/file-example")
def fileExample():
    return render_template("pages/file_example.html")

@app.route("/update-example")
def updateExample():
    query  = Query()
    result = query.selectByIdQuery(2)
    
    return render_template("pages/update_example.html", data=result)

@app.route("/submit-update", methods=['POST'])
def submitUpdateExample():
    setObject = SetObject(request.form['id'], request.form['name'], request.form['numCards'])
    query     = Query()
    query.updateQuery(request.form['id'], request.form['name'], request.form['numCards'])

    return render_template("pages/submit/update_example.html", data=setObject)

@app.route("/get-list-example")
def getListExample():
    query  = Query()
    result = query.selectListTable()

    return render_template("pages/get_list_example.html", data=result)

@app.route("/get-id-example/<id>")
def getExample(id):
    query  = Query()
    result = query.selectByIdQuery(id)

    return render_template("pages/get_id_example.html", data=result)

@app.route("/post-example")
def postExample():
    return render_template("pages/post_example.html")

@app.route("/submit-post", methods=['POST'])
def submitPostExample():
    query     = Query()
    result    = query.insertQuery(request.form['name'], request.form['numCards'])
    # get item info
    setObject = SetObject(result, request.form['name'], request.form['numCards'])

    return render_template("pages/submit/post_example.html", data=setObject)

@app.route("/delete-example/<id>")
def deleteExample(id):
    query  = Query()
    result = query.selectByIdQuery(id)

    return render_template("pages/delete_example.html", data=result)

@app.route("/submit-delete", methods=['POST'])
def submitDeleteExample():
    query  = Query()

    # delete
    result = query.deleteQuery(request.form['id'])
    # get item info - mark as deleted but not deleted from DB
    result = query.selectByIdQuery(request.form['id'])
    
    return render_template("pages/submit/delete_example.html", data=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
