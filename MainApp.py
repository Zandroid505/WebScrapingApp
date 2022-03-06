#
# Zakaria Antifit & Kobe Conomon
# March 5th, 2022
#

from flask import Flask, render_template, request
import base64
from io import BytesIO
from TemperatureFinder import *

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("Temperature.html")


@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return f"The URL /index is accessed directly. Try going to '/home' to submit form"
    if request.method == 'POST':
        # Get city from textbox
        city = request.form

        tf = TemperatureFinder(city.get("city"))

        # Assigning generated graph to fig
        fig = tf.manager()

        # Save it to a temporary buffer. (file object) (In UTF-8 encoding)
        buf = BytesIO()
        # Formatting buffer to png
        fig.savefig(buf, format="png")
        encoded_img = base64.b64encode(buf.getvalue())
        img_data = encoded_img.decode('utf-8')

        return render_template("Temperature.html", img_data=img_data, city=tf.city)


if __name__ == "__main__":
    app.run(debug=True)
