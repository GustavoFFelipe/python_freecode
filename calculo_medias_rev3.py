def ganho(horas, pagamento):
    print("Ganho por hora computado")
    if horas >= 40 :
        print("Hora extra.")
        #ganho em horas extras sendo 50% para cada hora a mais da carga horaria normal
        reg = horas * pagamento
        hextra= (horas - 40.0)* (pagamento * 0.5)
        pay= reg + hextra
        print("Seu ganho semanal foi:", pay)
        print("Sendo R$", reg, "Horas regulares." )
        print("E R$", hextra, "Horas extras.")
    else:
        #ganhos sem contagem de horas extras
        print("Horas regulares")
        pay = horas * pagamento
        print("Seu ganho semanal foi de:", pay)

    return pay




name= input("Qual seu nome?")
year= input("Qual sua idade?")
try:
    yyear= float(year)
except:
     print("Error, please enter a numeric number.")
     quit()
#entrar apenas com numeros
profissao= input("Qual sua sua profissão?")
print("Cadastro realizado com sucesso.")
print("Só mais algumas informações e vamos calcular seu ganho semanal.")

hsemanais= input("Quantas horas você trabalha por semana?")
phora= input("Quanto você recebe por hora trabalhada?")
try:
    hs= float(hsemanais)
    ph= float(phora)
except:
    print("Error, please enter a numeric number.")
    quit()
#print(hsemanais, phora)

print("Nome:", name)
print("Idade:", year)
print("Profissão:", profissao)
#converte o hs e ph para print xp que de ganho.
xp = ganho(hs, ph)
print(xp)
print('Boa semana!')
