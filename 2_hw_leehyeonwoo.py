number = int(input('4자리 정수를 입력하세요:'))
sum=0
a=number//1000
b=number//100%10
c=number//10%10
d=number%10
print('자리수 합은 {}이다.'.format(a+b+c+d))
