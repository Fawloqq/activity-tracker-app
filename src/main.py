from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///activities.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)


with app.app_context():
    db.create_all()


@app.route("/")
def index():

    activities = Activity.query.all()

    names = []
    times = []

    for activity in activities:
        if activity.end_time:
            duration = (activity.end_time - activity.start_time).seconds / 60
            names.append(activity.name)
            times.append(duration)

    return render_template(
        "index.html",
        activities=activities,
        names=names,
        times=times
    )


@app.route("/start", methods=["POST"])
def start():

    name = request.form["name"]

    activity = Activity(
        name=name,
        start_time=datetime.now(),
        end_time=None
    )

    db.session.add(activity)
    db.session.commit()

    return redirect("/")


@app.route("/stop/<int:id>")
def stop(id):

    activity = Activity.query.get(id)

    activity.end_time = datetime.now()

    db.session.commit()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    activity = Activity.query.get(id)

    db.session.delete(activity)
    db.session.commit()

    return redirect("/")


@app.route("/today")
def today():

    today_date = datetime.now().date()

    activities = Activity.query.filter(
        db.func.date(Activity.start_time) == today_date
    ).all()

    return render_template(
        "index.html",
        activities=activities,
        names=[],
        times=[]
    )


@app.route("/week")
def week():

    week_ago = datetime.now() - timedelta(days=7)

    activities = Activity.query.filter(
        Activity.start_time >= week_ago
    ).all()

    return render_template(
        "index.html",
        activities=activities,
        names=[],
        times=[]
    )


if __name__ == "__main__":
    app.run(debug=True)