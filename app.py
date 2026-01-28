from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def get_client_ip():
    if request.headers.get("X-Forwarded-For"):
        return request.headers.get("X-Forwarded-For").split(",")[0]
    return request.remote_addr

@app.route("/")
def home():
    ip = get_client_ip()
    user_agent = request.headers.get("User-Agent")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("visitors.log", "a") as f:
        f.write(f"{time} | IP: {ip} | UA: {user_agent}\n")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
