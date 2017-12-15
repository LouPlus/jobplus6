from flask import Blueprint

front = Blueprint('front',__name__)

@front.route('/')
def index():
   return render_template('index.html')
