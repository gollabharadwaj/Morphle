from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Golla Bharadwaj"
    username = os.getlogin()
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    
    top_output = subprocess.getoutput("top -bn1")

    # Get the dynamically assigned port
    port = os.getenv('PORT', 5000)

    page_content = f"""
    <h1>Server Information</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <p><b>Running on Port:</b> {port}</p>
    <pre>{top_output}</pre>
    """
    return page_content

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
