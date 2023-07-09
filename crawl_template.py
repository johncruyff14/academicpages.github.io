# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://northwestknives.com/"

# 发送HTTP请求
response = requests.get(url)

# 检查请求是否成功，HTTP状态码200表示成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 保存HTML内容到文件
    with open("template2.html", "w", encoding="utf-8") as file:
        # 写入HTML内容
        file.write(str(soup.prettify()))
else:
    print("Failed to retrieve webpage.")
