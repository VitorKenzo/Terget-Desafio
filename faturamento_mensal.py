#DADOS DO PROBLEMA
#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53
faturamento = {}
faturamento["SP"] = 67836.43
faturamento["RJ"] = 36678.66
faturamento["MG"] = 29229.88
faturamento["ES"] = 27165.48
faturamento["Outros"] = 19849.53

#calculo do total 
total = 0.0
for value in faturamento.values():
    total = total + value

#saida
print("Percentual de representação que cada estado:")
for key, value in faturamento.items():
    porcentagem = (value / total) * 100.00
    print(f"{key} - {porcentagem:.2f}%")



