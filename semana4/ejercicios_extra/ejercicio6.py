contador_hombres = 0
contador_mujeres = 0 
contador = 1
porcentaje_hombres = 0
porcentaje_mujeres = 0
print("Especifique el sexo de 6 personas")

while contador <= 6:
    sexo = int(input(f"Ingrese el sexo de la persona #{contador} (1 mujer / 2 hombre)"))
    if sexo == 1:
        contador_mujeres = contador_mujeres + 1
        contador = contador + 1
    elif sexo == 2:
        contador_hombres = contador_hombres + 1
        contador = contador + 1
    else:
        print("Ingrese una opción valida")
    
porcentaje_hombres = (contador_hombres / 6) * 100
porcentaje_mujeres = (contador_mujeres / 6 ) * 100
print(f"El porcentaje de hombres es {porcentaje_hombres}% y el porcentaje de mujeres es {porcentaje_mujeres}%")