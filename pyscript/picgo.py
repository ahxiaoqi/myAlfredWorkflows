import subprocess
import json

def upload():
    splitArr ="{query}".split("\t")
    cmd = 'curl -X POST -H "Content-Type: application/json" -d '
    jsonParam ='{"list": '+json.dumps(splitArr)+'}'
    output = subprocess.check_output(cmd+"'"+jsonParam+"' http://127.0.0.1:36677/upload", shell=True)
    resp = output.decode("utf-8").strip()
    return resp
    
str = json.loads(upload())["result"]
print(str)