n = int(input("支払い金額を入力してください: "))
x = int(input("商品価格を入力してください: "))

change = n - x

if change == 0:
    print('おつりは0円です。')

elif change > 0:
    a = change // 500
    b = change % 500
    c = b // 100
    d = b % 100
    e = d // 50
    f = d % 50
    g = f // 10
    print(f"おつりは500円玉{a}枚、100円玉{c}枚、50円玉{e}枚、10円玉{g}枚です。")

else:
    print('金額が足りません')