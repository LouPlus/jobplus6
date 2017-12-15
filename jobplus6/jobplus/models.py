from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    pass

class User(Base):
    pass

class Job(Base):
    pass

class Company(Base):
    pass
