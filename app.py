from flask import Flask, render_template

# The Flask application object
# Correctly point to the static and template folders inside the 'app' directory
app = Flask(__name__,
            static_folder='app/static',
            template_folder='app/templates')

# This route will now find and render your index.html page
@app.route('/')
def home():
    return render_template('index.html')

# This part is for local development and won't be used by Gunicorn/SWA
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)