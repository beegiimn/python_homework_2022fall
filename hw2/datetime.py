#Homework2 

import datetime
KhunboldBday = datetime.date(1995,8,28)
print(KhunboldBday)

b = datetime.date(1995,7,17)
d = datetime.date(1984,11,7)
dif =b-d
print (dif)

MomsBday = datetime.datetime.strptime('1963-09-22', '%Y-%m-%d')
print(MomsBday)