import sys, io
import cgi, cgitb
from html import escape
import json
from datetime import datetime
import logging

#now = datetime.now().strftime("%Y-%m-%d")
#logger = logging.getLogger('note.py')
#hdlr = logging.FileHandler('/log/note/note{now}.log'.format(now=now))
#formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#hdlr.setFormatter(formatter)
#logger.addHandler(hdlr) 
#logger.setLevel(logging.INFO)

def crlf2br(text):
    u"""改行文字を<br>に変更"""
    return text.replace("\r\n", "<br>").replace("<\n>", "<br>")

def get_formdata():
    u"""formから取得したデータをjson用にdictに変換
    存在しなければNoneを返す"""
    form = cgi.FieldStorage()
    time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    talker = form.getvalue("talker")
    note = form.getvalue("note")
    if note == None:
        return None
    formdata = {"time":time, "talker":talker, "note":note}
    #logging.info(formdata)
    return formdata

def make_disp_section(jsondata):
    u"""jsonデータを画面に表示するためにテーブルタグ文字列に変換"""
    section = ""
    with open("./cgi-bin/note/note_section.html", encoding="utf-8") as secthtml:
        srchtml = secthtml.read()
        for data in reversed(jsondata):
            time = data["time"]
            t = data["talker"].split(":")
            n = crlf2br(escape(data["note"]))
            section += srchtml[:].format(time=time, talker=t[0], note=n
                    , yomi=t[1])
    return section

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable(display=0, logdir="/log")

print('Content-type: text/html; charset=UTF-8\n')
with open("./cgi-bin/note/base.html", encoding="utf-8") as basehtml:
    htmltext = basehtml.read()

    try:
        jsondata = None
        path = "./cgi-bin/note/data/note.json"
        # ローカルのデータファイルから読み込み
        with open(path, encoding="utf-8") as jsonfile:
            jsondata = json.load(jsonfile)
            # フォームからデータを取得
            formdata = get_formdata()
            if formdata != None:
                # データに追加
                jsondata.append(formdata)
            # 画面に表示するためのHTML要素文字列を生成
            section = make_disp_section(jsondata)
            # 変換部分を要素文字列で置換
            htmltext = htmltext.replace("{{ NOTES }}", section)

        with open(path, "w", encoding="utf-8") as jsonfile:
            # 追加されたデータでローカルファイルを上書き
            json.dump(jsondata, jsonfile)
    except Exception as e:
        #logging.error(e)
        pass
    finally:
        # 最低限途中で処理が中断しても画面が描画される
        print(htmltext)

