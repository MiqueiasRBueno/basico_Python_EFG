# 1 - Construa um programa que seja capaz de pedir um número ao usuário, repetindo a pergunta caso o número
#  seja negativo e mostrando uma mensagem de sucesso caso seja positivo;

num_pos_usu = int(input("Digite um número inteiro positivo maior que zero: "))
while True:
    if num_pos_usu < 0:
        print(f"""Você digitou o número {num_pos_usu}.
O número digitado é um número negativo!""")
        num_pos_usu = int(input("Digite novamente: "))
    elif num_pos_usu == 0:
        print("Você digitou o número 0!")
        num_pos_usu = int(input("Digite novamente: "))
    else:
        if num_pos_usu > 0:
            print(f"""Você digitou o número {num_pos_usu}.
Este é um número positivo, parabéns!""")
            break
            