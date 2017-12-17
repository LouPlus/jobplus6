from flask import Blueprint,render_template
from flask import request, current_app
from jobplus.models import db, User, Job, Company

front = Blueprint('front',__name__)

@front.route('/')
def index():
   return render_template('index.html')
