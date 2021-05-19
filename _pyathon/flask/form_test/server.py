from flask import Flask, render_template , request , redirect , session
app=Flask(__name__)
app.secret_key="kep it secret"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users' , methods=["POST"])
def index2():
    session["name"] = request.form["name"]
    session["email"] = request.form["email"]
    return redirect("/show")

@app.route("/show")
def index3():
  
    return render_template("info.html", name = session["name"] , email = session["email"] )

if __name__ == "__main__":
    app.run(debug=True)