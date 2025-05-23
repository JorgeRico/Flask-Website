from flask import Flask, render_template, redirect, url_for
import requests
import json

class Api():
    headers = {"content-type": "application/json"}
    baseUrl = "https://api.restful-api.dev/"

app = Flask(__name__)
api = Api()


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
    requestUrl = api.baseUrl + "/objects/7"
    payload    = json.dumps({ "name": "Apple AirPods hhhhh", "data": { "color": "white", "generation": "3rd", "price": 135}})
    response   = requests.put(requestUrl, headers=api.headers, data=payload)

    return render_template("pages/update_example.html", data=json.loads(response.content))

@app.route("/patch-example")
def patchExample():
    requestUrl = api.baseUrl + "/objects/7"
    payload    = json.dumps({ "name": "Apple AirPods hhhhh" })
    response   = requests.patch(requestUrl, headers=api.headers, data=payload)

    return render_template("pages/update_example.html", data=json.loads(response.content))

@app.route("/get-list-example")
def getListExample():
    requestUrl = api.baseUrl + "/objects"
    response = requests.get(requestUrl, headers=api.headers)

    return render_template("pages/get_list_example.html", data=json.loads(response.content))

@app.route("/get-id-example")
def getExample():
    requestUrl = api.baseUrl + "/objects/7"
    response   = requests.get(requestUrl, headers=api.headers)

    return render_template("pages/get_id_example.html", data=json.loads(response.content))

@app.route("/post-example")
def postExample():
    requestUrl = api.baseUrl + "/objects"
    payload    = json.dumps({ "name": "Apple AirPods hhhhh", "data": { "color": "white", "generation": "3rd", "price": 135}})
    response   = requests.post(requestUrl, headers=api.headers, data=payload)

    return render_template("pages/post_example.html", data=json.loads(response.content))

@app.route("/delete-example")
def deleteExample():
    requestUrl = api.baseUrl + "/objects/7"
    response   = requests.patch(requestUrl, headers=api.headers)

    return render_template("pages/delete_example.html", data=json.loads(response.content))


if __name__ == "__main__":
    app.run(debug=True)