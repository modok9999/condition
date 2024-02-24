idvalue=input("id를 입력하세요")
pvalue=input("password를 입력하세요")



if len(idvalue)<=10:
    if len(pvalue)<=10:
        print("회원가입 성공")
    else:
        print("패스워드 10자리 초과")

else:print("아이디 10자리 초과")


    
