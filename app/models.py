from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class Employee(db.Model):
    __table__ = db.Model.metadata.tables['Employee']


class Album(db.Model):
    __table__ = db.Model.metadata.tables['Album']


class Artist(db.Model):
    __table__ = db.Model.metadata.tables['Artist']

class User(db.Model):
    __table__ = db.Model.metadata.tables['user']

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)