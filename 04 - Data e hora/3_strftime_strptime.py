from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y (%a) %H:%M"
mascara_ptbr_str = "%Y-%m-%d %H:%M"
mascara_en = "%Y-%m-%d %H:%M"

print()
print(data_hora_atual)
print()
print(data_hora_atual.strftime(mascara_ptbr))
print()
print(data_hora_atual.strftime("%y"))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print()
data_convertida = datetime.strptime(data_hora_str, mascara_ptbr_str)
print(data_convertida)
print()
print(type(data_convertida))
