import requests
import platform
from flask import Blueprint, request, jsonify

system = Blueprint("system_detail",__name__)


@system.route('/', methods=['GET', 'POST'])
def getSystemDetail():
            try:
                input_json = request.get_json(force=True) 
                dictToReturn = {'ip':input_json['ip']}
                ip = dictToReturn["ip"]
                
                # dictionary
                info = {}
                
                # platform details
                platform_details = platform.platform()
                
                # adding it to dictionary
                info["platform details"] = platform_details
                
                # system name
                system_name = platform.system()
                
                # adding it to dictionary
                info["system name"] = system_name
                
                # processor name
                processor_name = platform.processor()
                
                # adding it to dictionary
                info["processor name"] = processor_name
                
                # architectural detail
                architecture_details = platform.architecture()
                
                # adding it to dictionary
                info["architectural detail"] = architecture_details
                
                info["machine"] = platform.machine()
                
                    
                return info
        
            except:
                return jsonify(error=500, text="Internal Server error"), 500
            
