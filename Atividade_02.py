# Resposta 1 - Conversor de Moeda.
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em reais: R$", valor_reais)
print("Valor em dólares: US$", round(valor_dolar, 2))
print("Valor em euros: €", round(valor_euro, 2))

# Resposta 2 - Calculadora de Desconto.
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("\nNome do produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", porcentagem_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))

# Resposta 3 - Calculadora de Média Escolar.
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("\nNota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média final:", round(media, 2))

# Resposta 4 - Calculadora de Consumo de Combustível.
distancia = 300  # km
combustivel = 25  # litros

consumo_medio = distancia / combustivel

print("\nDistância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "litros")
print("Consumo médio:", round(consumo_medio, 2), "km/l")
