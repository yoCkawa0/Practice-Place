# # 画像用辞書
# items_imges = {
#     "剣": "http://paiza.jp/learning/images/sword.png",
#     "盾": "http://paiza.jp/learning/images/shield.png",
#     "回復薬": "http://paiza.jp/learning/images/potion.png",
#     "クリスタル": "http://paiza.jp/learning/images/crystal.png"
# }

# # ここから下を記述しよう
# # 出力するアイテム数を変数に代入
# item_cnt = int(input())
# # print(input())
# # 標準入力にあるアイテムを出力する
# while item_cnt > 0:
#     item = input()
#     # print(item)

#     print("<img src = '" + items_imges[item] + "'>")
#     item_cnt = item_cnt - 1
# 画像用辞書
import sys
items_imges = {
    "剣": "http://paiza.jp/learning/images/sword.png",
    "盾": "http://paiza.jp/learning/images/shield.png",
    "回復薬": "http://paiza.jp/learning/images/potion.png",
    "クリスタル": "http://paiza.jp/learning/images/crystal.png",
    # "6" : "http://paiza.jp/learning/images/crystal.png"
}

# ここから下を記述しよう
# items_order = ["剣","盾","回復薬","クリスタル"]
items_order = []
for i in sys.stdin.readlines():
    items_order.append(i.rstrip())
    # line = sys.stdin.readlines()

# print(items_order)


# for items_order in items_imges:
#     print("<img src =" +items_imges[items_order]+">")

for items_name in items_order:
    print("<img src ="+items_imges[items_name]+">")
