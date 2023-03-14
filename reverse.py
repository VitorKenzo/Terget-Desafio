#Entrada do usuario
string = input("Informe uma string: ")

#Invertendo a entrada
reversed_string = ""
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]

#saida
print("String invertida:", reversed_string)