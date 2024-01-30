import json
import sys

module_name_arr = ["文件管理","文档编辑","文件传输","磁盘管理","磁盘维护","网络通讯","系统管理","系统设置","备份压缩"]
def matchKeyWord(keyword):
    res_arr = []
    for m in module_name_arr:
        if keyword in m:
            res_arr.append(m)
    return res_arr


args = sys.argv;
if (len(args) > 0):
    strArr = matchKeyWord(args[1])
    items = []
    for moudleName in strArr:
        items.append({
                'title': moudleName,
                'subtitle': moudleName,
                'arg': moudleName,
                'icon': {'path': 'type.png'}
            })
    result = {}
    result["items"] = items
    print(json.dumps(result))