import sys, io
import cgi, cgitb

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable(display=0, logdir="/log")

print('Content-type: text/html; charset=UTF-8\n')

print(u"""\
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Text Converter</title>
    <link rel="stylesheet" href="/css/base.css">
    <link rel="shortcut icon" href="/img/icon_python.png">
    <script src="/script/common/util/timer.js"></script>
</head>
<body>
    <header>
        <h1>log.csvのテキストを配置してください。</h1>
        <span id="timer" style="font-size: 20px;"></span>
        <a href="/index.html">トップページ</a>
        <hr>
        <aside>先頭に定数を定義していない行のみ貼り付けてください。</aside>
    </header>

    <form method="post">
        <textarea id="area" name="oldtext" cols="175" rows="20" autofocus></textarea>
        <br>
        <input name="input" type="submit">
    </form>
    """)

form = cgi.FieldStorage()
if form.getvalue("oldtext"):
    val = form.getvalue("oldtext")
    from low2up import low2up
    newval = "".join([low2up(line) for line in val.split("\n")])
    print(u"""
            <br>
            <textarea cols="175" rows="20">{text}</textarea>
            """.format(text=newval))
else:
    print("please enter text to textarea.")

print("""
</body>
</html>
""")

