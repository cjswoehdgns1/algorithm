a=input()
b=1 if len(a)==1 else len(a)//2 # 한글자일때 0 출력되는 문제 수정
c=list(a)[:b]
d=list( list(a)[-b:].__reversed__() )
print(1 if c == d else 0)