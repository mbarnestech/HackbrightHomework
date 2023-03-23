import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    
    return render_template("index.html")


@app.route('/api/profile', methods=['POST'])
def profiles():
    """Return results from profile form."""

    result_dict = { 
        'name': request.json.get('name'), 
        'age': request.json['age'], 
        'occupation': request.json['occupation'], 
        'salary': request.json['salary'], 
        'education_level': request.json['educationLevel'], 
        'state': request.json['state'], 
        'city_type': request.json['cityType'], 
        'garden': request.json['garden'],
        'tv': request.json['tv']
        }
    # print(**result_dict)
    
    return jsonify(**result_dict)





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
