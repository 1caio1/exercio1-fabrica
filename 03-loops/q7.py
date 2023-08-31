entrada= input("digite o sexo")
homem=0
mulher=0
lista=[]
while entrada != 'sair':
    entrada= input("digite o sexo")
    if entrada== 'm':
        homem+=1
    elif entrada== 'f':
        mulher+= 1
    elif entrada=='sair':
        print("saindo...")


conta= homem+mulher
print("Quantidade total é: " ,conta, "Quantidade de homens é: " ,homem,  " Quantidade de mulheres é : " ,mulher)
