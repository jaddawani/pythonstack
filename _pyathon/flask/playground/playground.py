

from flask import Flask , render_template
app = Flask(__name__)    
@app.route('/play')          
def hello_world():
    return render_template("index.html")



@app.route('/play/<int:x>/<color>')          
def hello_world2(x,color):
    return render_template("index.html", num=x, color=color)








if __name__=="__main__":       
    app.run(debug=True)   