n=int(input(''))
sn=0
for i in range(1,n):
  if n%i==0:
    sn=i
if sn>1:
  print('yes')
elif n==1:
  print('no')
else:
  print('no')
