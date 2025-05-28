from flask import Flask, render_template, request
from models.database import Database

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
    db     = Database()
    query  = "SELECT id as id, name as name, numCards as numCards FROM mtgSet where id = 2;"
    result = db.getJsonData(query)   

    return render_template("pages/update_example.html", data=result[0])

@app.route("/submit-update", methods=['POST'])
def submitUpdateExample():
    item = {
        "id"       : request.form['id'], 
        "name"     : request.form['name'], 
        "numCards" :  request.form['numCards']
    }

    db    = Database()
    query = "UPDATE mtgSet SET id = %s, name = '%s', numCards = %s where id = %s;" %(request.form['id'], request.form['name'], request.form['numCards'], request.form['id'])
    db.updateData(query)

    return render_template("pages/submit/update_example.html", data=item)

# def createFakeItem(item):
#     # fake object need to be created to modify
#     # only fake created items can be edited
#     requestUrl = api.baseUrl + "/objects"
#     payload    = json.dumps(item)
#     response   = requests.post(requestUrl, headers=api.headers, data=payload)
#     postData   = json.loads(response.content)
#     # fake object need to be created to modify

#     return postData['id']

# @app.route("/patch-example")
# def patchExample():
#     requestUrl = api.baseUrl + "/objects/7"
#     payload    = json.dumps({ "name": "Apple AirPods hhhhh" })
#     response   = requests.patch(requestUrl, headers=api.headers, data=payload)

#     return render_template("pages/update_example.html", data=json.loads(response.content))

@app.route("/get-list-example")
def getListExample():
    db     = Database()
    query  = "SELECT id as id, name as name, numCards as numCards FROM mtgSet;"
    result = db.getJsonData(query)

    return render_template("pages/get_list_example.html", data=result)

@app.route("/get-id-example/<id>")
def getExample(id):
    db     = Database()
    query  = "SELECT id as id, name as name, numCards as numCards FROM mtgSet where id = %s;" %id
    result = db.getJsonData(query)

    return render_template("pages/get_id_example.html", data=result[0])

# @app.route("/post-example")
# def postExample():
#     return render_template("pages/post_example.html")

# @app.route("/submit-post", methods=['POST'])
# def submitPostExample():
#     item = { 
#         "name" : request.form['name'], 
#         "data" : { 
#             "color"      : request.form['color'], 
#             "generation" : request.form['generation'], 
#             "capacity"   : request.form['capacity'], 
#             "price"      : request.form['price']
#         }
#     }
    
#     requestUrl = api.baseUrl + "/objects"
#     payload    = json.dumps(item)
#     response   = requests.post(requestUrl, headers=api.headers, data=payload)

#     return render_template("pages/submit/post_example.html", data=json.loads(response.content))

# @app.route("/delete-example")
# def deleteExample():
#     requestUrl = api.baseUrl + "/objects/7"
#     response   = requests.patch(requestUrl, headers=api.headers)

#     return render_template("pages/delete_example.html", data=json.loads(response.content))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
