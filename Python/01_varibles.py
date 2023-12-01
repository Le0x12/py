#Variables---------
my_variable = "My string Variable"
print(my_variable)

my_int_variable = 33
print(type(my_int_variable))

my_converted_var_integer_to_string =str(3456)
print(type(my_converted_var_integer_to_string))

my_bool_variable = True
print(my_bool_variable)

print(my_int_variable, "es el valor de  " ,my_variable)
print(type(print("ola"))) #Non Type because is a function

#Funciones del sistema----
var_for_longer_type = "its a relative long string for test"
print("La cadena tiene de longitus ",len(var_for_longer_type)," contando espacios en blanco")


#Declaracion de Multivariable en ua linea (Praxis non good practices)----
name, last_name, age = "Lex", "Carrillo", 37
print("Mi nombre es",name, last_name, "y tengo", age,"años")


#inpunt on terminal 
name = input("What's your name?")
age = input("and your age?")

#For these case the value of the name and age change, this inclusive can change the type of value example int -> String 
#Python is not strong-type
print(name)
print(age)

address: str = "my forzed type declaration"
address = 32
print(type(address))

