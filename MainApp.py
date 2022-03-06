from flask import Flask
import base64
from io import BytesIO
from matplotlib.figure import Figure

import TemperatureFinder

app = Flask(__name__)


@app.route('/')
def index():
    # Assigning generated graph to fig
    fig = TemperatureFinder.manager()
    # Save it to a temporary buffer. (file object) (In UTF-8 encoding)
    buf = BytesIO()
    # Formatting buffer to png
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


if __name__ == "__main__":
    app.run(debug=True)
