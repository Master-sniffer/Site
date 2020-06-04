from flask import render_template, flash, redirect, url_for, abort
from flask import request
from flask_login import current_user, login_user
from flask_login import logout_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm
from app.models import User, Comments, Cinema
from app.forms import RegistrationForm
from app import db
from app import admin
from flask_admin.contrib.sqla import ModelView
from datetime import date
from app.forms import ResetPasswordRequestForm
from app.email import send_password_reset_email
from app.forms import ResetPasswordForm
from app.forms import CommentsForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('film'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('film')
        return redirect(next_page)
    return render_template('login.html', title='Sing In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('film'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('film'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


# @app.route('/index')
# @login_required
# def index():
#     return render_template("index.html", title='Home')

@app.route('/')
@app.route('/film')
def film():
    dates = date.today()
    q = request.args.get('q')
    if q:
        posts = Cinema.query.filter(Cinema.name.contains(q) | Cinema.theaters.contains(q)).all()
    else:
        posts = Cinema.query.order_by(Cinema.created.desc())

    return render_template('film.html', posts=posts, date=dates)


@app.route('/film/<film_name>', methods=['GET', 'POST'])
def film_info(film_name):
    post = Cinema.query.filter_by(name=film_name).first_or_404()
    form = CommentsForm()
    users = User
    user_comment = Comments.query.all()
    if form.validate_on_submit():
        add_comment = Comments(body=form.text.data, user_id=current_user.id)
        db.session.add(add_comment)
        db.session.commit()
    return render_template('film_info.html', post=post, form=form, comments=user_comment, user=users)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('film'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('film'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

class Check(ModelView):
    def is_accessible(self):
        if current_user.is_anonymous:
            return abort(404)
        if current_user.admin == True:
            return True
        else:
            return abort(404)

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


admin.add_view(Check(User, db.session))
admin.add_view(Check(Comments, db.session))
admin.add_view(Check(Cinema, db.session))
