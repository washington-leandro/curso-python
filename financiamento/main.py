# simulação de financiamento
casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
anos = int(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"Para pagar a casa de R${casa:.2f} em {anos} anos", end="" )
print(f" a prestação será de R${prestacao:.2f}.")

if prestacao <= minimo:
    print("O empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")