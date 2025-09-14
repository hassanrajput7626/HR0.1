# app.py
from flask import Flask, request, render_template, send_from_directory
import requests
import os

app = Flask(__name__)

# --------- Facebook Profile Fetch ------------
def get_profile_name(access_token):
    url = "https://graph.facebook.com/me"
    params = {'access_token': access_token}
    response = requests.get(url, params=params)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

# --------- Serve Local Videos ----------------
@app.route("/videos/<path:filename>")
def serve_video(filename):
    return send_from_directory("static/videos", filename)

# --------- Index Page ------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    profile_name = None
    error_message = None

    if request.method == 'POST':
        access_token = request.form['access_token']
        profile_name = get_profile_name(access_token)
        if profile_name is None:
            error_message = "Invalid access token. Please try again."

    return render_template('index.html', profile_name=profile_name, error_message=error_message)

# --------- Run Server ------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
