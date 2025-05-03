from datetime import datetime, timedelta, timezone as tz

data_oslo = datetime.now(tz(timedelta(hours=2)))
data_sao_paulo = datetime.now(tz(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)
