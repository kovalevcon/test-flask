from flask import Flask, render_template
import random

app = Flask(__name__)

# Array random string
array_strings = [
  "asjdgasdvh1hj23",
  "asdghjasg12nmbm",
  "13122312asdwetg",
  "daih23jkghasdjk"
]

@app.route("/")
def index():
    param = random.choice(array_strings)
    return render_template('index.html', param=param)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
