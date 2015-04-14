from flask import Blueprint, render_template
import webwatch, json, MySQLdb
from MySQLdb.cursors import DictCursor
mod = Blueprint('app', __name__, url_prefix='', template_folder="templates", static_folder="static")

@mod.route('/')
def index():
    return render_template("app.index.html")

@mod.route('/get_bus/<uuid>')
def get_bus(uuid):
    db = MySQLdb.connect(user="wirover", db="ibeacons", cursorclass=DictCursor)
    c = db.cursor()
    c.execute(
        "SELECT * FROM ibeacons WHERE uuid=%s",
        uuid,
    )
    measurementRows = c.fetchall()
    if not measurementRows:
        return json.dumps({ "error": "No beacons found" }), 404
    return json.dumps(measurementRows)

@mod.route('/get_bus_info/<vehicle_id>')
def get_bus_info(vehicle_id):
    return json.dumps(webwatch.get_bus(vehicle_id))