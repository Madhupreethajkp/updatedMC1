from flask import Flask
from flask_mail import Mail

#from app import app
from flask_mail import Mail, Message
app1 = Flask(__name__)

app1.config['MAIL_SERVER'] = 'smtp.gmail.com'
app1.config['MAIL_PORT'] = 465
app1.config['MAIL_USERNAME'] = 'mcpolicymanagementsystem@gmail.com'
app1.config['MAIL_DEFAULT_SENDER'] = 'mcpolicymanagementsystem@gmail.com'
app1.config['MAIL_PASSWORD'] = 'Policy@98'
app1.config['MAIL_USE_TLS'] = False
app1.config['MAIL_USE_SSL'] = True
app1.config['SECRET_KEY'] = 'madhu@98'
mail = Mail(app1)