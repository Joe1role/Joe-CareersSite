from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 2, "Data Analyst"
    'location': 3, "Atlanta"
    'salary': 4, "US. 250,000"
  }
  {
    'id': 2,
    'title': 2, "Software Engineer"
    'location': 3, "San Francisco"
    'salary': 4, "US. 450,000"
  }
  
]

@app.route("/")
def hello_joe():
  return render_template("home.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)