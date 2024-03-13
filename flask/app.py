from flask import Flask, render_template,request,flash,jsonify

app=Flask(__name__)


@app.route("/hello")
def index():
    return render_template("index.html")



@app.route("/<puneeth>")
def  send():
    return jsonify()


if __name__==__name__:     
    app.run()
