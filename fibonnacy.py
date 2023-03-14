def is_fibonacci(num):
    #caso base do 0
    if num == 0:
        return True
    
    #procurar pela sequencia se o numero esta dentro
    a, b = 0, 1
    while b <= num:
        #caso esteja
        if b == num:
            return True
        #iteracao
        a, b = b, a + b
    #se saiu do while nao esta na sequencia
    return False

#entrada do usuario
num = int(input("Digite um número: "))

if is_fibonacci(num):
    print("O número está na sequência de fibonacci")
else:
    print("O número não esta na sequência de fibonacci")