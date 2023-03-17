"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

MOODS = ['cheery', 'honest', 'dreary']

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template('form.html', moods = MOODS)

@app.route('/results')
def show_results():
    """Show resulting message."""

    checked_moods = request.args.getlist('mood')

    message = f'Have a {", ".join([mood for mood in checked_moods])} day'

    return render_template('results.html', message = message)

@app.route('/save-name')
def save_name():

    session['name'] = request.args.get('name')

    return render_template('homepage.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
