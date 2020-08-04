name= input("Qual seu nome?")
print('Nossas lojas: 1- São Paulo 2- Rio de Janeiro 3-Belo Horizonte.')
year= input("Qual loja você trabalha ?")
try: iyear= float(year)
except:
    print("Error, please enter a numeric number.")
#sal= input('Qual sua remuneração?')
#salario= float(sal)

tri1= input('Insira os ganhos no 1° Trimestre:')
tri2= input('Insira os ganhos no 2° Trimestre:')
tri3= input('Insira os ganhos no 3° Trimestre:')
tri11= float(tri1)
tri22= float(tri2)
tri33= float(tri3)
media= (tri11 + tri22 + tri33) / 3
print('Sua media anual de vendas foi:', media)

if media > 10000 :
    bonus=(media * 0.25)
    #bonus=(salario * 0.25)
    print('Parabéns, você alcançou a meta e recebeu um bônus de 25%')
    print('Seu bônus foi de R$', bonus)
    print('Aproveite seu bônus')

elif media >=7000 :
    bonus=(media * 0.10)
    #bonus=(salario * 0.10)
    print('Parabéns você alcançou a meta e recebeu um bonus de 10%!')
    print('Seu bônus foi de R$', bonus)
    print('Aproveite seu bônus.')
else :
    print("Infelizmente você não bateu sua meta, não desista e ira alcançar")
    print('Boa sorte!')
