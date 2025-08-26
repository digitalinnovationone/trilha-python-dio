from datetime import datetime

import pytz

data1 = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("Japan"))
data3 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data1)
print(data2)
print(data3)
