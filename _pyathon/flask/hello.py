from flask import Flask 
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  


@app.route('/dojo')          
def hello_world2():
    return 'Dojo!' 


@app.route('/<name>')          
def hello_name (name):
    return f"<h1> Hello {name} </h1>"




@app.route('/<int:num>/<name>')          
def repeat2 (num,name):
    str=f"<p>{name}</p>"
    for i in range (num):
        str+=f"<p>{name}</p>"
    
    return str

@app.route('/<num>/<name>')          
def repeat (num,name):
    return f"{name} "*int(num)


if __name__=="__main__":       
    app.run(debug=True)

