# Resposta 1 - Calculadora com validação e tratamento de erros

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero!")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida! Tente novamente.")
            continue

        print("Resultado:", resultado)
        break

    except ValueError:
        print("Erro: Entrada não numérica. Tente novamente.")

# Resposta 2 - Programa de registro de notas da turma

notas = []

print("\nDigite as notas da turma (ou 'fim' para encerrar):")
while True:
    entrada = input("Nota: ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número.")

if notas:
    media = sum(notas) / len(notas)
    print("Média da turma:", round(media, 2))
else:
    print("Nenhuma nota válida foi inserida.")

# Resposta 3 - Verificador de senha forte

import re

while True:
    senha = input("\nDigite a senha ou 'sair' para encerrar: ")
    if senha.lower() == 'sair':
        print("Encerrado.")
        break
    if len(senha) >= 8 and re.search(r'\d', senha):
        print("Senha forte!")
        break
    else:
        print("Senha fraca! Deve ter pelo menos 8 caracteres e um número.")

# Resposta 4 - Classificador de números pares e ímpares

pares = 0
impares = 0

print("\nDigite números inteiros (ou 'fim' para encerrar):")
while True:
    entrada = input("Número: ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Par")
            pares += 1
        else:
            print("Ímpar")
            impares += 1
    except ValueError:
        print("Erro: entrada inválida! Digite um número inteiro.")

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
