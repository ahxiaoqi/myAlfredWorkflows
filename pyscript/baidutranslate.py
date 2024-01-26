import random
import string
import hashlib
from urllib.parse import quote
import requests
import sys
import re

def contains_english(string):
    pattern = r'[a-zA-Z]'
    match = re.search(pattern, string)
    return match is not None



def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    return md5_hash.hexdigest()


# 调用函数生成长度为 length 的随机字符串
def generate_random_string(length):
    letters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

template = string.Template("http://api.fanyi.baidu.com/api/trans/vip/translate?q=$q&from=$froml&to=$to&appid=$appid&salt=$salt&sign=$sign")
signTemplate = string.Template("$appid$q$salt$key")

# def getResp():
#     url = buildUrl()
#     cmd = "curl "+ urlp
#     print(cmd)
#     output = subprocess.check_output(cmd, shell=True)
#     resp = output.decode("utf-8").strip()
#     return resp

def getResp(query):
    url = buildUrl(query)
    resp = requests.get(url)
    if(resp.status_code == 200):
        return resp.json()
    else:
        return ""

def buildUrl(query):
    ## 随机字符串
    randomStr = generate_random_string(10)
    ## 签名字符串
    signStr = signTemplate.substitute(appid="{appId}",q=query,salt=randomStr,key="{key}")
    ## md5签名
    md5_hash = calculate_md5(signStr)
    ## 最后的url地址
    froms = "zh"
    to = "en"
    if (contains_english(query)):
        froms = "en"
        to = "zh"
    return template.substitute(q=quote(query),froml=froms,to=to,appid="{appId}",salt=randomStr,sign=md5_hash)

args = sys.argv;
if (len(args) > 0):
    resp = getResp(args[1])["trans_result"]
    str = resp[0]["dst"]
    print(str)
# items = [{
#             'title': "idea",
#             'subtitle': str,
#             'arg': str,
#             'icon': {'path': 'ip.png'}
#         }]
# result = {}
# result["items"] = items
# print(json.dumps(result))