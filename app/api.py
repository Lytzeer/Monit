"""API for monit"""

from json import load
from flask import Flask, jsonify, redirect
from monit import get_report, get_all_reports, get_avg_of_report, get_last_rapport
from swagger_ui import api_doc


app = Flask(__name__)
api_doc(app, config_path="./swagger.yml", url_prefix="/api")


@app.route("/", methods=["GET"])
def index():
    """Index route"""
    return redirect("/api", code=302)


@app.route("/reports", methods=["GET"])
def reports():
    """All reports route"""
    return jsonify(get_all_reports()), 200


@app.route("/reports/<report_id>", methods=["GET"])
def report(report_id):
    """Report route"""
    return jsonify(get_report(report_id)), 200


@app.route("/reports/avg/<hours>", methods=["GET"])
def avg(hours):
    """Reports average x hours route"""
    return jsonify(get_avg_of_report(int(hours))), 200


@app.route("/reports/last", methods=["GET"])
def last():
    """Last report route"""
    return jsonify(get_last_rapport()), 200


if __name__ == "__main__":
    with open("/etc/monit/conf.d/api_conf.json", "r", encoding="utf-8") as f:
        config = load(f)
    app.run(host=config["host"], port=config["port"], debug=True)
