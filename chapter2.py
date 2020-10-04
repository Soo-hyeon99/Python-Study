#변수에 값 저장
a=20
b=30
c=a+b

print(c)

#올바른 변수명
x=20
Computer='Mac'
Age=30
my_score=70
_name='홍길동'

print(x, Computer, Age, my_score, _name)

#정수형의 데이터 형
x=30
print(x)
print(type(x))

#실수형의 데이터 형
x=3.3764
y=6/2

print(x, y)
print(type(x), type(y))

#문자열의 데이터 형
a='x'
b='I am ok.'
c="안녕하세요."

print(a)
print(b)
print(c)
print(type(c))

#30과 '30'의 차이
a=30
print(a)
print(type(a))

b='30'
print(b)
print(type(b))

#문자열의 요소 추출
x='I am happy!'

print(x)
print(x[0])
print(x[0:3])
print(x[5:])
print(x[-1])
print(x[-3:])
print(x[-4:-2])

#불(Bool) 데이터 형
a=True
b=False
print(a)
print(b)

c=10>20
print(c)

print(type(a))

#사칙 연산자
a=10
b=20

c=a+b*10-5/5
print(c)

#나머지 연산자와 소수점 절삭 연산자
x=10%3
print(x)

y=7//3
print(y)

#거듭제곱 연산자
x=2**3
print(x)

y=10**4
print(y)

#할당 연산자: +=
x=10
x+=20
print(x)

#할당 연산자: *=
x=3
y=5
x*=x+y
print(x)

#문자열 반복: * 곱셈기호 사용
hello='안녕'*5
print(hello)

#문자열 길이 구하기: len() 함수
a='쥐 구멍에 볕 들 날 있다.'
b=len(a)
print(b)

#문자열 연결 연산자: + 플러스 기호 <문자열을 + 연산자로 연결할 때에 사용되는 데이터 형은 모두 문자열이어야 한다.>
name='홍지수'
greet=name+'님 안녕하세요!'
print(greet)

#str() 함수: 정수형, 실수형 등의 변수 또는 데이터를 문자열로 변환하는 함수이다.
eng=80
result='영어점수: '+ str(eng) + '점'
print(result)

#문자열 포맷팅: %s
name='김수영'
a='나는 %s입니다.'%name
print(a)


#문자열 포맷팅: %d
age=20
a='나이는 %d살 입니다.' %age
print(a)

#정수형 숫자 0으로 채우기: %02d
year=2020
month=3
day=5

a='%d-%02d-%02d'%(year, month, day)
print(a)

#소수점 둘째 자리의 실수형 숫자: %.2f
height=155.2
a='키는 %.2f입니다.' %height
print(a)

#str.format() 문자열 포맷팅
name='황예린'
age=18
eyesight=1.2

a='이름: {}'.format(name)
b='나이: {}'.format(age)
c='시력: {}'.format(eyesight)

print(a)
print(b)
print(c)

#콤마(,)를 이용한 출력
name='홍길동'
age=30
height=173.7
print(name, age, height)

#문자열 연결 기호(+)를 이용한 출력
x=10
y=20
print('x = ' +str(x)+', y = ' + str(y))

#문자열 포맷팅(%)을 이용한 출력
score1 = 80
score2 = 87

sum = score1 + score2
avg = sum/2

print('두 과목 점수 : %d, %d' %(score1, score2))
print('합계: %d, 평균: %.2f' %(sum, avg))

#format()을 이용한 출력
name='김소원'
id='Kim'
point=18000

print('이름: {}'.format(name))
print('아이디: {}, 마일리지: {}'.format(id, point))

#키워드 sep을 이용한 출력
year=2020
month=3
day=5

print(year, month, day, sep='/')

#키워드 end를 이용한 출력
a='안녕하세요.'
b='반갑습니다.'

print(a)
print(b)
print('\n\n')
print(a, end=' ')
print(b)

#input()을 이용한 키보드 입력
name=input('이름을 입력하세요: ')
print('%s님 반갑습니다.'%name)

#입력받은 두 수의 합 구하기 : 잘못된 결과
a = input('첫 번째 숫자를 입력하세요 : ')
b = input('두 번째 숫자를 입력하세요 : ')

c=a+b

print(c)
print(type(a), type(b), type(c))

#잘못된 결과 수정하기
a = input('첫 번째 숫자를 입력하세요 : ')
b = input('두 번째 숫자를 입력하세요 : ')

c=int(a)+int(b)

print(c)

#데이터 형 변환에 사용되는 함수
#str(): 문자열로 변환
#int(): 정수형으로 변환
#float(): 실수형으로 변환

#키보드 입력된 인피를 센티미터로 변환
inch = float(input('인치(inch)를 입력하세요 : '))

cm = inch * 2.54

print('센티미터 : %.2f'%cm)
