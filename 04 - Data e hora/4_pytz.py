from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
data3= datetime.now(pytz.timezone("America/new_york"))
data4 = datetime.now(pytz.timezone("Asia/Tokyo"))

print("Oslo:", data)
print("São Paulo:", data2)
print("Nova Iorque:", data3)
print("Tóquio:", data4)    
