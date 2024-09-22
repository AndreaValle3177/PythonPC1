# Solicitar al usuario la hora
hora_input = input("Ingrese la hora (formato 24 horas, ej. 7:30): ")

# Convertir la hora a un número flotante
hora, minutos = map(int, hora_input.split(':'))
hora_float = hora + minutos / 60

# Determinar la comida correspondiente
if 7.0 <= hora_float <= 8.0:
    print("Es hora de desayunar.")
elif 12.0 <= hora_float <= 13.0:
    print("Es hora de almorzar.")
elif 18.0 <= hora_float <= 19.0:
    print("Es hora de cenar.")
