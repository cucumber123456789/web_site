from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Список пользователей (лучше хранить в базе данных)
users = {
    "username1": "password1",
    "username2": "password2"
}

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if users.get(username) == password:
        return "Вы успешно вошли как {}".format(username)
    else:
        return "Неверное имя пользователя или пароль"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    users[username] = password

    return "Вы успешно зарегистрировались как {}".format(username)

if __name__ == '__main__':
    app.run()
