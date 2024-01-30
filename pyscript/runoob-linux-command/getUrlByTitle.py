import json
import sys
import os

# 是否需要从指定的模块里面找
moudleName = os.environ.get('moudleName','')

def buildIndex():
   with open('./pyscript/resources/noob-linux-command.json','r') as file:
        urlMap = json.load(file)
        return urlMap

urlJson = buildIndex()

args = sys.argv;
if (len(args) > 0):
    keyword = args[1]  
    if '' != moudleName:
        items = []
        for item in urlJson[moudleName].keys():
             if keyword in item: items.append({
                'title': item,
                'subtitle': moudleName,
                'arg': urlJson[moudleName][item],
                'icon': {'type': 'filetype', 'path': 'icon.png'}
            })
        result = {}
        result["items"] = items
        print(json.dumps(result))
    else:
        items = []
        for moudleName in urlJson.keys():
            moudleNameInfo = urlJson[moudleName]
            for item in moudleNameInfo.keys():
             if keyword in item: items.append({
                'title': item,
                'subtitle': moudleName,
                'arg': moudleNameInfo[item],
                'icon': {'path': 'command-line.png'}
            })
        result = {}
        result["items"] = items
        print(json.dumps(result))  