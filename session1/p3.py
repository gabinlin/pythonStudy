chinaNumber = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
num = input()
showText = ''
for i in range(len(num)):
    showText += chinaNumber[eval(num[i])]
print(showText)
