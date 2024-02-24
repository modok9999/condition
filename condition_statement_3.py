number1=int(input("첫번쨰 숫자를 입력해주세요>>>"))
number2=int(input("두번쨰 숫자를 입력해주세요>>>"))
number3=int(input("세번쨰 숫자를 입력해주세요>>>"))
max_value=0

if number1>number2 and number1>number3:
   max_value=number1
elif number2>number1 and number2>number3:
   max_value=number2
else:10
   max_value=number3
# print("가장 큰 수는",max_value,"입니다.")
print(f"가장 큰 수는 {max_value}입니다.사용자가 입력한 수{number1}{number2}{number3}")