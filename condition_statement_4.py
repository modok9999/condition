import math
name=input("학생의 이름을 입력해주세요>>>")
s1=int(input("국어점수 입력해주세요>>>"))
s2=int(input("영어점수 입력해주세요>>>"))
s3=int(input("수학점수 입력해주세요>>>"))
escore=0
sname=""

if s1<0 or s1>100:
    # if not 0<s1<100
    # print(f"{name}:국어점수 입력 오류입니다. 입력값{s1}")
    escore=s1
    sname="국어"
elif s2<0 or s2>100:
#    print(f"{name}:영어점수 입력 오류입니다. 입력값{s2}")
   escore=s2
   sname="영어"
elif s3<0 or s3>100:
#    print(f"{name}:수학점수 입력 오류입니다. 입력값{s3}")
   escore=s3
   sname="수학"

else:
   total=s1+s2+s3
   avg=(total)/3
   result=80-avg
   escore==0
   if avg>=80: 
    print(f"{name}:보충학습 아님")
   else:
    print(f"{name}:보충학습 대상, 점수차:",round(result),"점") 

if escore !=0:
   print(f"{name}:{sname}점수 입력 오류입니다. 입력값{escore}")

print("점수 유효성체크 완료")




