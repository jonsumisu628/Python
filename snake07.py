# coding: utf-8
x = 1
if x == 1:
    print("焼きそば")     # xが1だったら焼きそば
else:
    print("ラーメン")     # xが1以外ならラーメンと出力する


y = 2
if y == 1:
    print("焼きそば")
elif y == 2:
    print("うどん")       # yが2ならうどんと出力する条件式を追加
else:                     # 2つ以上条件があるときはelifを使う
    print("ラーメン")

z = 3
if z > 6:
    print("りんご")       # zが6より大きいときはりんごと出力
elif z > 3:
    print("みかん")       # zが3より大きいときはみかんと出力
elif z > 1:
    print("ばなな")       # zが1より大きいときはばななと出力
else:
    print("ドラゴンフルーツ")  # zがすべての条件を満たさないときはドラゴンフルーツと出力

# a == b   aとbは等しい(aはbである)
# a != b   aはbと等しくない(aはbではない)
# a > b    aはbより大きい(aはbに含まれない)
# a < b    aはbより小さい(aはbに含まれない)
# a >= b   aはb以上(aはbに含まれる)
# a <= b   aはb以下(aはbに含まれる)


import random
n = random.randint(1,9)   # 1〜9の数値をランダムで出力
if n == 1:
    print(str(n) + "位!" + "金メダル")  # nが1なら金メダル
elif n == 2:
    print(str(n) + "位!" + "銀メダル")  # nが2なら銀メダル
elif n == 3:
    print(str(n) + "位!" + "銅メダル")  # nが3なら銅メダル
elif n >= 7:
    print(str(n) + "位!" + "残念賞")    # nが7以上なら残念賞
else:
    print(str(n) + "位!" + "頑張ったでしょう")  # それ以外は頑張ったでしょう(4,5,6位)
