from flask import Flask, render_template, redirect, abort, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from data import db_session
from data.users import User, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/Frilans.db")
    app.run()

@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(User).all()
    names = dict()
    for job in jobs:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        names[job.team_leader] = user.surname + ' ' + user.name
    return render_template("index.html", jobs=jobs, names=names, title="Марсиане")

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()