from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms import SignupForm
from app import db
from app.models import Artist
bp_main = Blueprint('main', __name__)


@bp_main.route('/')
@bp_main.route('/index')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        from app.models import User
        user = User(user_id='1', username=form.first_name.data, email=form.email.data,)
        user.set_password(form.password.data)
        from sqlalchemy.exc import IntegrityError
        try:
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and try again.'.format(
                form.name.data), 'error')
    return render_template('signup.html', form=form)

@bp_main.route('/artists', methods=['GET'])
def artists():
   artist_list = Artist.query.all()
   return render_template("artists.html", artists=artist_list)