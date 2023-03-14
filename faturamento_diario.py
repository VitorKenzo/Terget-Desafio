import json

# lendo dados do json
with open('dados.json', 'r') as json_file:
    data = json.load(json_file)

# variaveis auxiliares
faturamento = {}
dias_validos = 0
faturamento_total = 0.0
# preenchendo dicionario
for item in data:

    dia = item["dia"]
    valor = item["valor"]

    if (valor != 0):
        faturamento[dia] = valor
        faturamento_total = faturamento_total + valor
        dias_validos = dias_validos + 1

# calculo do maior faturamento
maior_faturamento = max(faturamento.values())
# calculo do menor faturamento
menor_faturamento = min(faturamento.values())
# prints
print(f"O maior faturamento foi de {maior_faturamento}")
print(f"O menor faturamento foi de {menor_faturamento}")

# calculo dos dias acima da media
media_faturamento = faturamento_total / dias_validos
dias_acima_media = []
for key, value in faturamento.items():
    if value >= media_faturamento:
        dias_acima_media.append(key)
print(f"Dias acima da média foram {dias_acima_media}")
