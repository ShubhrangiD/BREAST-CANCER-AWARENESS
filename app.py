from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pickle
from functools import wraps

# Load the model
model = pickle.load(open("model.pkl", 'rb'))

# Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for session management

# Dummy credentials for demonstration
USERNAME = 'admin'
PASSWORD = 'password'

# Decorator to ensure user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method == 'POST':
        features = [
            'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 
            'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 
            'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se', 
            'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 
            'compactness_worst', 'concavity_worst', 'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst', 
            'other_feature'
        ]
        
        try:
            input_data = [float(request.form[feature]) for feature in features]
        except ValueError:
            return redirect(url_for('home'))  # Handle conversion errors gracefully
        
        np_features = np.array(input_data).reshape(1, -1)
        pred = model.predict(np_features)
        message = 'Cancerous' if pred[0] == 1 else 'Not Cancerous'
        
        return redirect(url_for('result', message=message))
    
    # For GET request, render the index.html page with the form
    return render_template('predict.html')

@app.route('/result')
@login_required
def result():
    message = request.args.get('message')
    return render_template('result.html', message=message)

@app.route('/about')
@login_required
def about_breast_cancer():
    return render_template('about.html')

@app.route('/data-analysis')
@login_required
def data_analysis():
    return render_template('data-analysis.html')

@app.route('/resources')
@login_required
def resources():
    return render_template('resources.html')

@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

@app.route('/research')
@login_required
def research():
    return render_template('research.html')

@app.route('/faq')
@login_required
def faq():
    return render_template('faq.html')

@app.route('/forum')
@login_required
def forum():
    return render_template('forum.html')

@app.route('/about_us')
@login_required
def about_us():
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run(debug=True)
