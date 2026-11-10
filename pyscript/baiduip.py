import subprocess
import json

def getBaiDuip(ip):
    cmd = f"curl  --location --request GET 'https://qifu.baidu.com/api/v1/ip-portrait/brief-info?ip={ip}' --header 'Referer: https://qifu.baidu.com/?_frm=aladdin&activeId=SEARCH_IP_ADDRESS&ip={ip}' "
    output = subprocess.check_output(cmd, shell=True)
    resp = output.decode("utf-8").strip()
    return resp
resp = json.loads(getBaiDuip("{query}")).get("data") or {}

def field(key):
    value = resp.get(key)
    return str(value) if value is not None else ""

str = field("country") + field("province") + field("city") + field("isp")
items = [{
            'title': "{query}",
            'subtitle': str,
            'arg': str,
            'icon': {'type': 'filetype', 'path': 'icon.png'}
        }]
result = {}
result["items"] = items
print(json.dumps(result))