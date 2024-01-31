import re
import json
import sqlite3
import os
userDir = os.getenv('userDir')

dbpath = "/Users/"+userDir+"/Library/Messages/chat.db"
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()
cursor.execute('SELECT text FROM message WHERE datetime(date/1000000000 + 978307200,"unixepoch","localtime") > datetime("now","localtime","-60 second") ORDER BY date DESC limit 1;')
result = cursor.fetchall()
items = []
if (len(result) == 1):
    message = str(result[0][0])
    #message = "614530 ,这是您的动态验证码，5分钟内有效【12321】"
    # 使用正则表达式提取数字部分
    match = re.findall(r'(?<![[-【])\d{4,}(?![\]】])', message)
    
    if match:
        for code in match:
            items.append({
                'title': code,
                'subtitle': message,
                'arg': code,
                'icon': {'path': 'message-code.png'}
                })
else:
    items.append({
                'title': '暂无验证码',
                'subtitle': '暂无验证码',
                'arg': '',
                'icon': {'path': 'None.png'}
                })

result = {}    
result["items"] = items
print(json.dumps(result)) 
cursor.close()
conn.close()
