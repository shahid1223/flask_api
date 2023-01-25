import requests
import re
import socket
from flask import Blueprint, request, jsonify
import geocoder


from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

latLonByIp = Blueprint("lat_long_by_ip",__name__)


def is_valid_ip(ip):
    # Regular expression to match valid IP addresses
    pattern = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    if re.match(pattern, ip):
        return True
    return False

@latLonByIp.route('/', methods=['GET', 'POST'])
def getlatlong():
            try:
                input_json = request.get_json(force=True) 
                dictToReturn = {'ip':input_json['ip']}
                ip = dictToReturn["ip"]
                
                if is_valid_ip(ip):
                    
                    url = "http://ip-api.com/json/"+ip+"?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
                    response = requests.get(url)
                    data = response.json()
                    return data
                else:
                    return jsonify(error=404, text=f"{ip} is not a valid IP address."), 404 
        
            except:
                return jsonify(error=500, text="Internal Server error"), 500
            
@latLonByIp.route('/ipstack', methods=['GET', 'POST'])
def getLatLongByIpstack():
        
        if request.method == 'POST':
            try:
                input_json = request.get_json(force=True)
                dictToReturn = {'ip':input_json['ip']}
                ip = dictToReturn["ip"]
                if is_valid_ip(ip):
                    url = f"http://api.ipstack.com/"+ip+"?access_key=3cf98190d0873802d729935236852504"
                    response = requests.get(url)
                    data = response.json()
                    return data
                else:
                    return jsonify(error=404, text=f"{ip} is not a valid IP address."), 404 
        
            except:
                return jsonify(error=500, text="Internal Server error"), 500
            
            
@latLonByIp.route('/geocoder', methods=['POST','GET'])
def dataByGeocoder():
            try:
                input_json = request.get_json(force=True) 
                dictToReturn = {'ip':input_json['ip']}
                ip = dictToReturn["ip"]
                
                if is_valid_ip(ip):
                    
                    #by geocoder
                    g = geocoder.ip(ip)
                    myLatLng = g.latlng
                    location = geolocator.reverse(str(myLatLng[0])+","+str(myLatLng[1]))
                    
                    address = location.raw['address']
                    address['lat'] = myLatLng[0]
                    address['lng'] = myLatLng[1]
                    address['address'] = str(location)
                    
                    return address
                
                else:
                    return jsonify(error=404, text=f"{ip} is not a valid IP address."), 404 
        
            except:
                return jsonify(error=500, text="Internal Server error"), 500
            
@latLonByIp.route('/geolocationdb', methods=['POST','GET'])
def dataByGeolocationDb():
            try:
                    input_json = request.get_json(force=True) 
                    location = location = geolocator.reverse(str(input_json['latitude'])+","+str(input_json['longitude']))
                    data = location.raw['address']
                    data.update(input_json)
                    return data
            except:
                return jsonify(error=500, text="Internal Server error"), 500
        
  
