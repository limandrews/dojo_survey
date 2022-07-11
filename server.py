from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "anystringiwantas"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    session["name"] = request.form["usernamebox"]
    session["location"] = request.form["locationbox"]
    session["language"] = request.form["languagebox"]
    session["comments"] = request.form["commentbox"]
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True)