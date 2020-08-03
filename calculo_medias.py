name= input("Qual seu nome?")
year= input("Qual sua idade?")
profissao= input("Qual sua sua profissão?")
print("Cadastro realizado com sucesso.")
print("Só mais algumas informações e vamos calcular seu ganho semanal.")

hsemanais= input("Quantas horas você trabalha por semana?")
phora= input("Quanto você recebe por hora trabalhada?")
hs= float(hsemanais)
ph= float(phora)

#print(hsemanais, phora)

print("Nome:", name)
print("Idade:", year)
print("Profissão:", profissao)
if hs > 40 :
    print("Hora extra.")
    #ganho em horas extras sendo 50% para cada hora a mais da carga horaria normal
    reg= hs * ph
    hextra= (hs - 40.0)* (ph * 0.5)
    total= reg + hextra
    print("Seu ganho semanal foi:", total)
    print("Sendo R$", reg, "Horas regulares." )
    print("E R$", hextra, "Horas extras.")
else:
    #ganhos sem contagem de horas extras
    print("Horas regulares")
    reg= hs * ph
    print("Seu ganho semanal foi de:", reg)
