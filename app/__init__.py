from os.path import dirname, abspath, join

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfdQbTOExternjy5xmCNaA'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CWD = dirname(abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(CWD, 'chinook.sqlite')
    db.init_app(app)
    # The following is needed if you want to map classes to an existing database
    with app.app_context():
        db.Model.metadata.reflect(db.engine)
    # If you don't have a database with records that you created in ex1 then you all need to create the database tables by uncommenting the following lines
    from app.models import Employee, Album, Artist
    with app.app_context():
        db.create_all()

     # Register Blueprints
    from app.routes import bp_main
    app.register_blueprint(bp_main)

    return app
