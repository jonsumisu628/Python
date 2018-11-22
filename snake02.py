# coding: utf-8
#HTMLを表示する
#出力タイプをhtmlにする
print("<h1>hello world</h1>")
print("<p>世界の皆さん,")
print("<b>こんにちは</b></p>")

print('''<h1>hello world</h1>
<p>世界の皆さん,
<b>こんにちは</b></p>''')

print("<h1>hello world</h1>","<p>世界の皆さん,","<b>こんにちは</b></p>")

print("<h1>hello world</h1>", end="")
print("<p>世界の皆さん,", end="")        # ""の中に何か入力すれば文末に表示される
print("<b>こんにちは</b></p>", end="")

# すべて同じ表示