# coding: utf-8
# 文字列同士で+を使うと文字が結合する
x = "ご褒美"
y = "カフェオレ"
print(x + y)

# 文字列に*を使うとその分繰り返す
d = "お茶"
print(d * 5)

# 数値同士はただの計算になる
z = 123
v = 456
print(z + v)

# ""で囲うと文字列扱いになる
m = "123"
n = "456"
print(m + n)

# この場合は数値と文字列でデータ型が違うのでエラーがでる
# g = 123
# q =  "カフェオレ"
# print(g + q)

# str()で囲ってやると文字列に変換できる
# 一時的に変換されるだけで上書きされているわけではない
g = 123
q = "カフェオレ"
print(str(g) + q)