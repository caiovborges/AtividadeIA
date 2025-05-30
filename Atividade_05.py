# Resposta 1 - Função para calcular gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

# Exemplo de uso:
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem de gorjeta: "))
resultado = calcular_gorjeta(valor, porcentagem)
print("O valor da gorjeta é: R$", resultado)


# Resposta 2 - Função para verificar se é palíndromo

import re

def eh_palindromo(texto):
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return texto_limpo == texto_limpo[::-1]

# Exemplo de uso:
frase = input("\nDigite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("Sim, é um palíndromo!")
else:
    print("Não, não é um palíndromo.")


# Resposta 3 - Função para calcular idade em dias

from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    dias = idade * 365
    return dias


ano = int(input("\nDigite seu ano de nascimento: "))
idade_dias = calcular_idade_em_dias(ano)
print("Sua idade aproximada em dias é:", idade_dias)
