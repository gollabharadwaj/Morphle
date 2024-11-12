from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():

    full_name = "Bharadwaj Golla"

  
    username = os.getenv("USER") or os.getlogin()

 
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')


    top_output = subprocess.getoutput("top -bn 1")

 
    response = f"""
    <p><b>Name:</b> {full_name}</p>
    <p><b>user:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre><Strong>TOP OUTPUT:</Strong>\n\n{top_output}</pre>

    """
    return response

if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port=5000)
