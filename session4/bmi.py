#!/usr/bin/python3
# bmi demo
height, weight = eval(input("请输入身高(米)和体重(KG)，用逗号(英文符号)隔开\n"))
bmi = weight / pow(height, 2)
print("bmi数值:{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who = nat = "偏瘦"
elif 18.5 <= bmi < 24:
    who = nat = "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who = nat = "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who = nat = "肥胖"
print(who, nat)