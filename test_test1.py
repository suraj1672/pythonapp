from flask import Flask 
app = flask(_name_)


@app.route("/")
def home():
  return "Hello this code was updated locally and pushed to Azure Devops repo"
