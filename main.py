from test import fn
from flask import Flask, render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/data',methods=['POST'])
def data():
    n=request.form['btn']
    y=request.form['emp_id']
    x=request.form['name']
    z=request.form['btn1']
    fn(x,y,n,z)
    return "Thanks"


if __name__=='__main__':
    app.run(debug=True,host='10.133.48.6',port='3000')
