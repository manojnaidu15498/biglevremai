n1,op1=map(int, input().split())
n2,op2=map(int, input().split())
n3,op3=map(int, input().split())
if n1>op1:
    diff1=n1-op1
else:
    diff1=op1-n1
    print(diff1)
if n2>op2:
    diff2=n2-op2
else:
    diff2=op2-n2
    print(diff2)
if n3>op3:
    diff3=n3-op3
else:
    diff3=op3-n3
    print(diff3)
