#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Name: SearchPlus.py
# Powered by KurisuCat

from sanic import Sanic
from sanic.response import html
from jinja2 import Template, FileSystemLoader, Environment
import subprocess
from urllib.parse import unquote
import os


app = Sanic("SearchPlus")

templateFolder = FileSystemLoader('./template')  # 设置 jinja 的模板文件路径
templateEnvironment = Environment(loader=templateFolder)  # 设置环境
template = templateEnvironment.get_template('main.html')  # 设置模板


@app.route("/<SearchText:str>")
@app.get("/")
async def searchPlus(request, SearchText=""):
    def 检测是否连接互联网():
        if os.name == "nt":
            checker, return_data = subprocess.getstatusoutput(
                "ping -n 1 -w 200 google.com")
        else:
            checker, return_data = subprocess.getstatusoutput(
                "ping -W 200 google.com")
        if checker == 0:
            return True
        else:
            return False

    def 模板(SearchEngine, SearchText, haveText, engineURL):
        return template.render(Engine=SearchEngine, Text=unquote(SearchText), haveText=haveText, engineURL=engineURL)

    def 分流(SearchText, haveText):
        if 检测是否连接互联网():
            SearchEngine = "Google Search"
            engineURL = "https://www.google.com/search?q="
            return 模板(SearchEngine, SearchText, haveText, engineURL)
        else:
            SearchEngine = "百度一下"
            engineURL = "https://www.baidu.com/s?wd="
            return 模板(SearchEngine, SearchText, haveText, engineURL)
    if SearchText == "":
        haveText = "False"
        pageResult = 分流(SearchText, haveText)
    else:
        haveText = "True"
        pageResult = 分流(SearchText, haveText)
    return html(pageResult)

# if os.name == "nt":
#     import PySimpleGUI as gui
#     gui.theme('SystemDefaultForReal')
#     layout = [[gui.Text('SearchPlus 启动器')],
#               [gui.Text('如需停止运行请在任务管理器中停止运行')],
#               [gui.Text('复制右边的 URL 可添加到浏览器'), gui.InputText(
#                   default_text="https://127.0.0.1/%s")],
#               [gui.Text('添加搜索引擎（Chrome）'), gui.InputText(
#                   default_text="chrome://settings/searchEngines")],
#               [gui.OK(button_text='不再提示'), gui.Cancel(button_text='我知道了', focus=True)]]
#     window = gui.Window('SearchPlus - 自动切换百度和谷歌的小工具', layout,
#                         size=(600, 150), grab_anywhere=True)
#     while True:
#         event, values = window.read()
#         if event == gui.WIN_CLOSED or event == '我知道了':
#             break
#         if event == '不再提示':
#             break
#     window.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6722, fast=True, auto_reload=True)
