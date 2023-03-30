"""Sample Flask app for SQLAlchemy homework."""

from flask import Flask, render_template
from model import connect_to_db
from model import all_employees_nav, all_employees_join


app = Flask(__name__)
app.secret_key = 'ABCSECRETDEF'


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')


@app.route('/emps-nav')
def emps_nav():
    """Show directory, using object navigation."""

    results = all_employees_nav()
    return render_template("directory-nav.html", employees=results)


@app.route('/emps-join')
def emps_join():
    """Show directory, using single SQL join."""

    results = all_employees_join()
    return render_template("directory-join.html", employees=results)


if __name__ == "__main__":

    connect_to_db(app)

    app.run(debug=True, host='0.0.0.0')
