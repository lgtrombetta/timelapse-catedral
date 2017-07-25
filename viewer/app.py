from flask import Flask, render_template, url_for
from subprocess import call
from shutil import move
from time import sleep


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('capture.html')

@app.route('/capture/')
def capture():
    call(["gphoto2","--capture-image-and-download"]) 
    sleep(2)
    move("capt0000.jpg", "static/img/capt0000.jpg")
    sleep(1)
    return render_template('capture.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

