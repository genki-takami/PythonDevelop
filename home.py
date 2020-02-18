import calculate as c

your_salary=float(input("あなたの年収を教えて下さい（数字のみ）："))
supouse_yes_no=int(input("\n現在、配偶者の方はいますか？\nYesなら数字の1を、Noなら数字の0をお願いします："))
support_yes_no=int(input("\n現在、扶養している方はいますか？\nYesなら数字の1を、Noなら数字の0をお願いします："))
if support_yes_no==1:
    supported_1=int(input("\n4つの質問に答えてください\n扶養している方の中に16歳以上19歳未満の方は何人いますか？（数字のみ）："))
    supported_2=int(input("扶養している方の中に19歳以上23歳未満の方は何人いますか？（数字のみ）："))
    supported_3=int(input("扶養している方の中に70歳以上の同居老親の方は何人いますか？（数字のみ）："))
    supported_4=int(input("扶養している方の中に70歳以上の別居老親の方は何人いますか？（数字のみ）："))
else:
    supported_1=0
    supported_2=0
    supported_3=0
    supported_4=0
your_condition=int(input("\n現在、障害を抱えていますか？\nYesなら数字の1を、Noなら数字の0をお願いします："))
your_status=int(input("\n現在、就労しながら教育機関に所属していますか？\nYesなら数字の1を、Noなら数字の0をお願いします："))
life_insurance=float(input("\n年間の支払い生命保険料を教えてください（数字のみ）："))
your_resident=input("\nあなたの住んでいる都道府県をローマ字半角小文字（例:tokyo）で教えてください：")



a = c.cal_disposal_income(your_salary)
my_disposal_income=a.disposable_income(supported_1,supported_2,supported_3,supported_4,supouse_yes_no,your_condition,your_status,your_resident,life_insurance)
my_disposal_income/=12
print(f"\n\n＞＞＞あなたの1ヶ月の可処分所得は{int(my_disposal_income):,}円です！!")
print(“hello!world”)
