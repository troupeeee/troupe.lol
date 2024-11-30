from flask import Flask, request
import datetime

app = Flask(__name__)

LOG_FILE = "ip_logs.txt"

@app.route('/log-ip', methods=['GET'])
def log_ip():
    visitor_ip = request.remote_addr
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{timestamp} - IP: {visitor_ip}\n")
    
    return "IP logged successfully", 200

@app.route('/view-logs', methods=['GET'])
def view_logs():
    with open(LOG_FILE, "r") as log_file:
        logs = log_file.read()
    return f"<pre>{logs}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
