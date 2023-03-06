nome = str(input("Qual o seu nome? "))
idade = int(input("Qual a sua idade? "))
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura em metros? "))
imc = float((peso/(altura**2)))

print(nome, "tem", idade, "anos", "pesa", peso, "mede", altura, "E seu IMC e de", imc)
