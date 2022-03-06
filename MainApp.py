#
# Zakaria Antifit & Kobe Conomon
# March 5th, 2022
#

from flask import Flask, render_template
import base64
from io import BytesIO
from matplotlib.figure import Figure

from TemperatureFinder import *

app = Flask(__name__)


@app.route("/")
def index():
    tf = TemperatureFinder()

    # Assigning generated graph to fig
    fig = tf.manager()
    # Save it to a temporary buffer. (file object) (In UTF-8 encoding)
    buf = BytesIO()
    # Formatting buffer to png
    fig.savefig(buf, format="png")
    encoded_img = base64.b64encode(buf.getvalue())

    return render_template("Temperature.html", img_data=encoded_img.decode('utf-8'))


if __name__ == "__main__":
    app.run(debug=True)
