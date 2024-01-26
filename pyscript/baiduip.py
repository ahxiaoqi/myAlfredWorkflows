import subprocess
import json

def getBaiDuip(ip):
    cmd = "curl https://qifu-api.baidubce.com/ip/geo/v1/district?ip="+ip
    output = subprocess.check_output(cmd, shell=True)
    resp = output.decode("utf-8").strip()
    return resp
resp = json.loads(getBaiDuip("{query}"))["data"]
str = resp["prov"]+resp["city"]+resp["district"]
items = [{
            'title': "{query}",
            'subtitle': str,
            'arg': str,
            'icon': {'type': 'filetype', 'path': 'icon.png'}
        }]
result = {}
result["items"] = items
print(json.dumps(result))