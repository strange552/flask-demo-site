from flask import Flask, render_template, request
import logging
from datetime import datetime


app = Flask(__name__)

# Logging setup
logging.basicConfig(filename='access.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    app.logger.info("Home page visited from %s", request.remote_addr)
    return render_template("index.html")

@app.route('/about')
def about():
    app.logger.info("About page visited from %s", request.remote_addr)
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

