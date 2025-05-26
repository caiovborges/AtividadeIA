# Resposta 1 - Classificador de Idade.
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    classificacao = "Criança"
elif idade >= 13 and idade <= 17:
    classificacao = "Adolescente"
elif idade >= 18 and idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print("Classificação:", classificacao)

# Resposta 2 - Calculadora de IMC.
peso = float(input("\nDigite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("Seu IMC é:", round(imc, 2))
print("Classificação:", classificacao)

# Resposta 3 - Conversor de Temperatura.
temperatura = float(input("\nDigite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()

resultado = None

if origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura
elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado = ((temperatura - 32) * 5/9) + 273.15
    else:
        resultado = temperatura
elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura

print("Temperatura convertida:", round(resultado, 2), destino)

# Resposta 4 - Verificador de Ano Bissexto.
ano = int(input("\nDigite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    resultado = "Bissexto"
else:
    resultado = "Não é bissexto"

print("O ano", ano, "é:", resultado)
