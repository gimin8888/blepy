import math

dfmoney = 50000
df = 180
samsib = 7000

finaltime = int(input('최종 작업물 시간을 적으시오. '))

remaintime = (finaltime - df)

num3 = int(remaintime)/30

num4 = math.ceil(num3)

num5 = (num4 * samsib)

num6 = (num5 + dfmoney)

print(num6)