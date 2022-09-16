#Homework2 

import datetime
from re import A, M
KhunboldBday = datetime.date(1995,8,28)
print(KhunboldBday)

b = datetime.date(1995,7,17)
d = datetime.date(1984,11,7)
dif =b-d
print (dif)

# 2nd assignment of homework
MomsBday = datetime.datetime.strptime('1963-09-22', '%Y-%m-%d') #string to datetime
print(MomsBday)
type(MomsBday)

DadsBday = datetime.datetime(1963,10,18) #datetime to string
print("a",DadsBday)
type(a)

