print("Este é um menu de opções")
print(" ")
num1 = float(input('Digite o número para calcular: '))
num2 = float(input('Digite o segundo número para calcular: '))
opcao = 0
while opcao != 6:
    print(""" 1 - Somar
        2 - Dividir
        3 - multipicar
        4 - subtrair
        5 - Inserir novos números]
        6 - Sair""")
    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        soma = num1 + num2
        print("A soma entre {} + {} é {}.".format(num1,num2, soma))
    elif opcao == 2:
        div = num1 / num2
        print("A divisão entre {} + {} é {}.".format(num1,num2, div))
    elif opcao == 3:
        multi = num1 * num2
        print("A multiplicação entre {} + {} é {}.".format(num1,num2, multi))
    elif opcao == 4:
        sub = num1 - num2
        print("A subtração entre {} + {} é {}.".format(num1,num2, sub))
    elif opcao == 5:
        print("Digite novamente")
        num1 = float(input('Digite o número para calcular: '))
        num2 = float(input('Digite o segundo número para calcular: '))
    elif opcao == 6:
        print("Fim do programa")
    else: 
        print("Opção inválida")
print ("Fim, volte sempre")
"""
def soma(num1,num2):
    return num1+num2
def divisao(num1,num2):
    return num1/num2

print(soma)

print(divisao)
"""