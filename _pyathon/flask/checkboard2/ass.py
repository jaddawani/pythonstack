from flask import Flask  , render_template
app = Flask(__name__)   
@app.route('/hey/<int:x>/<int:y>/<color>')          
def hello_world(x,y,color):
    return render_template("index.html", column=x,row=y,color=color)  
if __name__=="__main__":    
    app.run(debug=True)    