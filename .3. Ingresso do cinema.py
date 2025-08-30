idade = int(input("Digite sua idade: "))

if idade <= 13:
    print("O ingresso é R$10")
elif idade >= 13 and idade <= 59:
    print("O ingresso é 20R$")
elif idade >=60:
    print("O ingresso é R$12")
