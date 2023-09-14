from flask import Flask, render_template,request,flash
app=Flask(__name__)

@app.route("/hello")
def index():
    return render_template("index.html")

if __name__==__name__:     
    app.run(debug=True)
