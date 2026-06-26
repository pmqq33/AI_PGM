score = int(input("점수를 입력하세요 : "))

if score >= 90 :
    print("학점은 A입니다.")
elif score >= 80 :
    print("학점은 B입니다.")
elif score >= 70 :
    print("학점은 C입니다.")
elif score >= 60 :
    print("학점은 D입니다.")    
else :
    print("학점은 F입니다.")

ent = 10000
age = int(input("나이를 입력하세요 : "))

if age >= 20:
    ent = ent + ent * 0.1

print(f"입장료는 {ent}원입니다.")

money = int(input("얼마를 가지고 있나요? : "))

if money >= 10000 :
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
money = True

if money :
    print("택시를 타고 가라")
else :
    print("걸어가라")

