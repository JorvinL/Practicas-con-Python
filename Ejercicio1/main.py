# Coding UTF-8
_author_ = 'Jorvin'

# Scrip de consola para calcular la edad segun la fecha de nacimiento

print ("Bienbenido, este programa te dirá tu edad\n")
print ("Para continuar, completa el formulario...\nUsa el formato dd/mm/aaaa\n\n")

dia_de_nacimiento = int(input("día de nacimiento: "))
mes_de_nacimiento = int(input("mes de nacimiento: "))
año_de_nacimiento = int(input("año de nacimiento: "))

año_actual = 2022
mes_actual = 10
dia_actual = 19

if mes_actual >= mes_de_nacimiento:
    meses_de_mas = mes_actual - mes_de_nacimiento
else:
    meses_de_mas = mes_de_nacimiento - mes_actual
    
if dia_actual >= dia_de_nacimiento:
    dias_de_mas = dia_actual - dia_de_nacimiento
else:
    dias_de_mas = dia_de_nacimiento - dia_actual
    
edad = año_actual - año_de_nacimiento

meses_de_masEnAños = meses_de_mas / 12
dias_de_masEnAños = dias_de_mas /365

edadExacta = int(edad + meses_de_masEnAños + dias_de_masEnAños)

print ("\nTu edad actual es de {} años, {} meses, y {} días..".format(edadExacta, meses_de_mas, dias_de_mas))