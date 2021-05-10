from flask import Flask , render_template
app = Flask(__name__)    
@app.route('/play')          
def hello_world():
    return render_template("index.html")

@app.route('/play/<int:x>')          
def hello(x):
    return render_template("index2.html", y=x)


@app.route('/play/<int:x>/<f>')          
def hello_color(x,f):
    f=f
    
    return render_template("index3.html", y=x, f=f)






if __name__=="__main__":       
    app.run(debug=True)   