import redis
import secrets
from flask import Flask
from flask_session import Session
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix='/')
app.secret_key= secrets.token_hex()

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://127.0.0.1:6379')


server_session = Session(app)

if __name__ == '__main__':
    app.run(debug=True)

