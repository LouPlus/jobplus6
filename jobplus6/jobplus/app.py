from flask import Flask,render_template
from jobplus.config import configs
from jobplus.models import db

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)

    register_blueprints(app)

    return app
   


'''test
app = Flask(__name__)

@app.route('/')
def job():
    return 'Hello jobplus!'
if __name__ == '__main__':
    app.run()
'''
'''
class Job(db.Model):
    __tablename__ = "job"
    id = db.Column(db.Integer,primary_key=True)
    jobname = db.Column(db.String(32),unique=True,index=True,nullable=False)

@app.route('/')
def index():
    jobs = Job.query.all()
    return render_template('/templates/index.html',jobs=jobs)

if __name__ == '__main__':
    app.run()
'''
