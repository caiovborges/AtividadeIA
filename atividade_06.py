
# Atividade Prática 06 


import statistics

tempos = []

with open('log_treinamento.txt', 'r') as arquivo:
    for linha in arquivo:
        try:
            tempo = float(linha.strip())
            tempos.append(tempo)
        except ValueError:
            continue 

if tempos:
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0
    print("Média do tempo de execução:", round(media, 2))
    print("Desvio padrão:", round(desvio, 2))
else:
    print("Nenhum dado válido encontrado no arquivo.")


import csv

pessoas = [
    {"Nome": "Ana", "Idade": 25, "Cidade": "Salvador"},
    {"Nome": "Bruno", "Idade": 30, "Cidade": "Recife"},
    {"Nome": "Carla", "Idade": 22, "Cidade": "Fortaleza"}
]

with open('pessoas.csv', 'w', newline='') as csvfile:
    campos = ['Nome', 'Idade', 'Cidade']
    writer = csv.DictWriter(csvfile, fieldnames=campos)

    writer.writeheader()
    for pessoa in pessoas:
        writer.writerow(pessoa)

print("Arquivo 'pessoas.csv' criado com sucesso.")

with open('pessoas.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print("Dados do arquivo CSV:")
    for row in reader:
        print(f"Nome: {row['Nome']}, Idade: {row['Idade']}, Cidade: {row['Cidade']}")


import json

pessoa = {
    "nome": "João",
    "idade": 28,
    "cidade": "Rio de Janeiro"
}

with open('pessoa.json', 'w') as jsonfile:
    json.dump(pessoa, jsonfile, indent=4)

print("Dados salvos em 'pessoa.json'.")

with open('pessoa.json', 'r') as jsonfile:
    dados = json.load(jsonfile)
    print("Dados lidos do arquivo JSON:")
    print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")
