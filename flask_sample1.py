from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/life-skills")
def home():
    return {"empowerment": 
    [   "Familial", 
        "Emotional",
        "Social",
        "Vocational",
        "Physical",
        "Financial",
        "Spiritual"
    ]}