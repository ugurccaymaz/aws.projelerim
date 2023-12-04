from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html',number1=2,number2=34)


@app.route('/malt')
def number():
    x=500
    y=250
    return render_template('body.html',value1=x,value2=y,sum=x*y)


if __name__== "__main__":
    #app.run(debug=True, port=30000)
     app.run(host= '0.0.0.0', port=8081)