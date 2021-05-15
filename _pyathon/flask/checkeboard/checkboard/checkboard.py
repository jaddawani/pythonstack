from flask import Flask , render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def checkboard():
#     return render_template('home.html',rows=8,column=8
#     )  # Return the string 'Hello World!' as a response


@app.route('/')  
@app.route('/<x>/<y>')   
       
def checkboard1(x=8,y=8):
    return render_template('home.html',rows=int(x),column=int(y)
    )  # Return the string 'Hello World!' as a response








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.