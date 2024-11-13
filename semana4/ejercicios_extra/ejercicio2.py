print("Calculadora de tiempo en segundos")
tiempo_en_segundos = int(input("Ingrese el tiempo en segundos: "))
diez_minutos = 600
segundos_faltantes = 0   

if tiempo_en_segundos < diez_minutos:
    segundos_faltantes = diez_minutos - tiempo_en_segundos
    print(f"Faltarian {segundos_faltantes} segundos para llegar a 10 minutos")
else:
    print("El tiempo en segundos es mayor a diez minutos")