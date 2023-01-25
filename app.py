from flask import Flask
from pages.lat_long_by_ip import latLonByIp
from pages.system_detail import system
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(latLonByIp,url_prefix="/clientip")
app.register_blueprint(system,url_prefix="/systemdetail")

if __name__ == '__main__':
    app.run(debug = True, port=5002)