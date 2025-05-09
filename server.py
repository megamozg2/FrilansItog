from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/Frilans.db")
    app.run()

@app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(users).all()
#     names = dict()
#     for job in jobs:
#         user = db_sess.query(User).filter(User.id == job.team_leader).first()
#         names[job.team_leader] = user.surname + ' ' + user.name
#     return render_template("index.html", jobs=jobs, names=names, title="Марсиане")


if __name__ == '__main__':
    main()