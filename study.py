# print(type("hello"))
# print(type(234))
# print(type(True))
# print(type(36.322))
## type 정리

# print('"배가고프다"라고 생각함')
## 큰따옴표나 작은따옴표를 내부에 사용하면 그냥 프린트가 됨

# print('\'이스케이프 문자 사용으로 따옴표 쓰기\'')

# print("탭\t사용")
# print("줄바꿈\n사용")

# print("""\
#       의도하지 않는 
#       줄바꿈이 싫을때
#       이렇게 따옴표 세개와 
#       역슬래시를 사용한다\
#       """)

##문자열(스페이스도 포함된다)연산자와 인덱스 , 연산자는 +-* 다 가능하며 숫자랑 붙일때는 따옴표를 통해서 강제로 str로 변환후 사용한다
# print("문자열 연산자 " + "1")
# print("문자열 연산자 "*3)
# print("문자열 인덱스"[1])
# print("문자열 인덱스"[-1])
# print("문자열 인덱스"[0:3])
# print("문자열 인덱스"[:5])

##문자열 길이
# print(len("문자열의 길이를 구하는 방법"))

# print(0.5e2) // e2 = 10^2

##연산자 
#/ = 나누기 // = 몫  % = 나머지  ** = 제곱 ////    연산순서는 곱셈 나눗셈우선으로 앞에서 부터 진행한다.

##복합대입연산자
# +=, -=, *=, /=, %=, **= 
# 전부 계산후 대입하는것임 
# a+=10 == a=a+10


##input, 자료형 변경
# ia = float(input("첫 번째 숫자> "))
# ib = float(input("두 번째 숫자> "))


# print("덧셈 결과: ",ia + ib)
# print("뺄셈 결과: ",ia-ib)
# print("곱셈 결과: ",ia*ib)
# print("나눗셈 결과: ",ia/ib)

##format() {}개수랑 .format()의 소괄호 개수가 동일해야 함
# format_a = "{}만원으로 {}만원 만들기".format(100,200)
# print(format_a)

oa = "{:+5d}".format(50)
ob = "{:-5d}".format(50)
oc = "{:=+5d}".format(50)
od = "{:=+5d}".format(-50)
oe = "{:+05d}".format(50)
of = "{:-05d}".format(50)

print("#format조합")
print(oa)
print(ob)
print(oc)
print(od)
print(oe)
print(of)