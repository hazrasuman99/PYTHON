from flask import Flask, render_template, url_for, request
from flask_wtf import Form
from wtforms.fields import TextField
from wtforms.fields import SubmitField
from wtforms.fields import PasswordField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'I_LOVE_PIZZA'

class UserForm(Form):
    username = TextField("UserName")
    password = PasswordField("Password")
    submit = SubmitField("Enter Credentials")

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = UserForm()
    if request.method == 'POST':
        return render_template('display.html')
    return render_template('upload.html', form = form)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)