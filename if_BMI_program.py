#practice  Calculate BMI
#BMI = weight(kg)/(height(m)*height(m))
#note my issue:
#1: 轉型
#2: if elis else 後面要有 :
#3: else if 在 python 是 elif
#4: print 怎麼輸入再一次 ex: print("weight:70(kg), height:1.80(m)")

height = input("請輸入身高: ")
height = float(height)
height = height/100

weight = input("請輸入體重: ")
weight = float(weight)

BMI = weight/(height*height)
print("weight: ", weight, " (kg)")
print("height: ", height, " (m)")
print("BMI: ", BMI)

if BMI < 18.5:
    print("體重過輕")
elif BMI >= 18.5 and BMI < 24:
    print("正常")
elif BMI >= 24 and BMI < 27:
    print("過重")
elif BMI >=27 and BMI < 30:
    print("輕度肥胖")
elif BMI >= 30 and BMI < 35:
    print("中度肥胖")
else:
    print("重度肥胖")

