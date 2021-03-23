from flask import Flask, request, session,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel
from flask_cors import CORS
from flask_login import LoginManager

app = Flask()
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
CORS(app)

# Initialize babel
babel = Babel(app)

class User(db.Model) :
    id          = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)
    password    = db.Column(db.String(128))
    auth           = db.Column(db.String(100))
    email          = db.Column(EmailType, unique=True, nullable=False)
    nickname       = db.Column(db.String(100), nullable=False)

    @property
    def is_authenticated(self):
        return True
    @property
    def is_admin(self) :
        if self.auth == u'admin' :
            return True
        else :
            return False
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.session_protection='strong'

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
    
    @login_manager.unauthorized_handler
    def unauthorized() :
        return make_response(jsonify(success=False),401)

    @app.before_request
    def app_before_request() :
        if 'client_id' not in session:
            session['client_id'] = request.environ.get('HTTP_X_REAL_IP',request.remote_addr)

@babel.localeselector
def get_locale():
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    return session.get('lang', 'ko')

init_login()

