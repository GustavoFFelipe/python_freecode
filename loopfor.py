print('Você esta a procura de carros de luxo ou carros populares?')
decision = input('1 - Carros populares           2 - Carros de luxo: ')
decision1 = float(decision)
if decision1 == 1:
    cars = ["1-Honda Civic - R$ 70.000", "2-Chevrolet Onix - R$ 35.000", "3-Toyota Hilux - R$ 120.000",
     "4-Mitsubish L200 - R$ 100.000", "5-Fiat Chronos - R$ 70.000", '6-Volkswagem Golf - R$ 100.000']
    for cars in cars:
        print(cars)
else:
    carsluxo = ['1-Porshe Cayman - R$ 300.000', '2-Ferrari Sport Enzo - R$ 500.000', '3-Porshe Carrera S - R$ 400.000',
    '4-Lamborgini Veneno - R$ 700.000', '5-Audi A6 - R$ 350.000', '6-Mclaren M3 - R$ 457.000']

    for carsluxo in carsluxo:
        print(carsluxo)
print('Gostou de algum? Simule um financiamento')
name = input('Qual o seu nome?')
fin = input('Qual carro você mais gostou? ')
tel = input('Deixe seu telefone para contato também: ')
print('Obrigado pela preferência, entraremos em contao em breve')
