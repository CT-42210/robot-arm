from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-time')
def get_time():
    # Get the current time and format it
    time = datetime.datetime.now().strftime('%H:%M:%S')
    # Return the time as a response to the client
    return time


if __name__ == '__main__':
    app.run(port=6969)
