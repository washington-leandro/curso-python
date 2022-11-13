def fatorial(numero):
    fatorial = 1
    for i  in range(2, numero+1):
        fatorial*= i
    return fatorial

valor = int(input("Insira um número para calcular o seu fatorial: "))
print(f"O fatorial de",valor," é:",fatorial(valor))