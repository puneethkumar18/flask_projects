from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/fail/<float:score>')
def fail(score):
    return render_template('result.html',marks = score,result = 'Fail')

@app.route('/success/<float:score>')
def success(score):
    return render_template('result.html',marks = score,result = 'Pass')

@app.route('/submit',methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        Data = float(request.form['data'])
        social = float(request.form['social'])
    total_score = (science+maths+Data+social)/4
    res = ''
    if total_score > 50:
        res = 'success'
    else:
        res = 'fail'
    return redirect(url_for(res,score = total_score))



if __name__ == '__main__':
    app.run(debug=True)