import subprocess
import json

def getBaiDuip(ip):
    cmd = f"curl  --location --request GET 'https://qifu.baidu.com/api/v1/ip-portrait/brief-info?ip={ip}' --header 'Referer: https://qifu.baidu.com/?_frm=aladdin&activeId=SEARCH_IP_ADDRESS&ip={ip}' "
    output = subprocess.check_output(cmd, shell=True)
    resp = output.decode("utf-8").strip()
    return resp
resp = json.loads(getBaiDuip("{query}"))["data"]
str = resp["country"]+resp["province"]+resp["city"]+resp["isp"]
items = [{
            'title': "{query}",
            'subtitle': str,
            'arg': str,
            'icon': {'type': 'filetype', 'path': 'icon.png'}
        }]
result = {}
result["items"] = items
print(json.dumps(result))