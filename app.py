from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'data anaylyst',
    'location': 'bengaluru , india',
    'salary': 'rs1000bdfkjfj'
}, {
    'id': 2,
    'title': 'front ed engineer',
    'location': 'bengaluru , india',
    'salary': 'rs1000bdfkjfj'
}, {
    'id': 3,
    'title': 'backend ',
    'location': 'bengaluru , india',
    'salary': 'rs1000bdfkjfj'
}, {
    'id': 4,
    'title': 'anaylyst',
    'location': 'bengaluru , india',
    'salary': 'rs1000bdfkjfj'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
