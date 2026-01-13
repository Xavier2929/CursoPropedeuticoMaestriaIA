#proceso llamado SLICING
# Sirve para extraer porciones de caracteres o textos como quiera verse.

texto = "ABCDEFGHIJKLMN"
fragmento = texto[2]
fragmento2 = texto[3:] #obtiene desde la posicion 3 hasta el final
fragmento3 = texto[:3] # obtiene desde el inicio hasta la posicion 3
print(fragmento2) 
print(fragmento3)
fragment4 = texto[2:5]
print(fragment4)


print("corte en secuencia")

corte_de_dos_en_dos = texto[: : 2] # crea una cadena agarrando el char cada 2 caracteres
print(corte_de_dos_en_dos)


corte_de_dos_en_dos = texto[: : -2] # de dos en dos, pero de reversa
print(corte_de_dos_en_dos)

print("Funcion de .index() ")

texto = "esta es una prueba"
text_con_index = texto.index("a")
print(text_con_index)

numeros = (1,2,3,2,5,2)
numbers_w_index = numeros.index(3,0,5)

print(numbers_w_index)

print("metodo upper")
texto= "Hoy vamos a ver seis metodos"
uppder_result = texto.upper()
print(f'este es la variable normal \n "{texto}" y a uppder es \n {uppder_result}')

print("metodo lower")
lower_result = texto.lower()
print(f'este es la variable normal \n "{texto}" y a lower es \n "{lower_result}"')


print("ahora veremos el metodo split")
split_result = texto.split(' ')
print(split_result)
print(texto.split('o') )

print("ahora vamos a usar join()")

list_to_reverse_to_str = ['Hoy', 'vamos', 'a', 'ver', 'seis', 'metodos']
joined_list = " ".join(list_to_reverse_to_str)
print(joined_list)

print("metodo find")
print(joined_list.find("metodo"))

print("metodo replace()")

print(joined_list.replace("metodo","calacas"))

print("metodo isdecimal()")
print("2.55".isdecimal())

print("metodo isalnum")
print("123ABC".isalnum())

print("metodo isalnum()")
print("123ABC".isalpha())

print("metodo isspace()")
print("  ".isspace())

print("metodo capitalize()")
print("hi .mom!".capitalize())

print("metmdo swapcase() ")
print("Hi Everyone!".swapcase())