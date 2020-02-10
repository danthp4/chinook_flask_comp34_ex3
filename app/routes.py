from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms import SignupForm

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
@bp_main.route('/index')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Signup requested for {}'.format(form.last_name.data))
    # Code to add the student to the database goes here
        return redirect(url_for('main.index'))
    return render_template('signup.html', form=form)

@bp_main.route('/courses', methods=['GET'])
def courses():
   course_list = Course.query.all()
   return render_template("courses.html", courses=course_list)