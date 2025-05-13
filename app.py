from flask import Flask, request

app = Flask(__name__)
db_info_test = {}

@app.route("/post-test", methods=["POST"])
def post_test():
    global db_info_test
    json = request.get_json()
    db_info_test = json
    return json

@app.route("/get-test", methods=["GET"])
def get_test():
    return db_info_test if db_info_test else "There's no post"

# Model for JSON
"""
{
    "title_date": "13/05/2025",
    "title_day": "Tuesday",
    "system_status": {
        "energy_level": 10,
        "mental_clarity": 1,
        "physical_readiness": 8,
        "emotional_state": 6,
        "hours_of_sleep": 3
    }
}"""