from flask import Flask, jsonify, request
from monit import get_report, get_all_reports, get_avg_of_report, get_last_rapport
import json

app = Flask(__name__)

@app.route("/reports", methods=["GET"])
def reports():
    return jsonify(get_all_reports()),200

@app.route("/reports/<id>", methods=["GET"])
def report(id):
    return jsonify(get_report(id)), 200

@app.route("/reports/avg/<hours>", methods=["GET"])
def avg(hours):
    return jsonify(get_avg_of_report(int(hours))), 200

@app.route("/reports/last", methods=["GET"])
def last():
    return jsonify(get_last_rapport()), 200


if __name__ == "__main__":
    with open("/etc/monit/conf.d/api_conf.json", "r") as f:
        config = json.load(f)
    app.run(host=config["host"], port=config["port"], debug=True)