nome = str(input("Qual o seu nome? "))
idade = int(input("Qual a sua idade? "))
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura em metros? "))
imc = float((peso/(altura**2)))

print(f"{nome} tem {idade} anos, pesa {peso:.2f}kg, mede{altura: .2f}m e seu IMC e de {imc: .2f}")
# f de formatacao .2f significa duas casas apos a virgula

