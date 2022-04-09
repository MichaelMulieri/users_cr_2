from flask import Flask, render_template, redirect, request
from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def all_users():
    return render_template('users.html', users=User.get_all())

@app.route('/users/create')
def add_user():
    return render_template('new_users.html')

@app.route('/user/new', methods=['POST'])
def save_user():
    User.save(request.form)
    print(request.form)
    return redirect ('/users')


if __name__ == "__main__":
    app.run(debug=True)