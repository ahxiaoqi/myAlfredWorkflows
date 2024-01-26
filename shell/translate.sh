#!/bin/bash

string="{query}"



if  [[ $string =~ ^[[:alpha:]]+$ ]]; then
    #echo "字符串只包含英文字符"
	echo -n "input={query}&from=en_US&to=zh_CN" | shortcuts run  "翻译"
else
    #echo "字符串包含非英文字符"
	echo -n "input={query}&to=en_US&from=zh_CN" | shortcuts run  "翻译"
fi


