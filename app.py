#Instructions: in the windows terminal go to this directory and type:
# > set FLASK_APP = app.py
# > flask run

from flask import Flask, render_template_string
import grapher

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8" />
<title>Test</title>
</head>

<body>

Data: <span id="data"><span>

<script type="text/javascript">
var data_span = document.getElementById("data");

function updater() {
  fetch('/data')
  .then(response => response.text())
  .then(text => (data_span.innerHTML = text));  // update page with new data
}

setInterval(updater, 1000);  // run `updater()` every 1000ms (1s)
</script>

</body>

</html>""")

@app.route('/data')
def data():
    """send current content"""
    return str(grapher.getArray())


if __name__ == "__main__":
    app.run(debug=True)

