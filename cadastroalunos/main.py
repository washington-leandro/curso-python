def filtrar_sexo (dados):
  for dados in lista_alf:
    if dados['sexo'].upper() == 'FEMININO':
      feminino.append(dados.copy())
    else:
      masculino.append(dados)

def mostrar_alunos (feminino, masculino):
  if len(feminino):
    x = '\nLista das alunas'
    print('-' * len(x))
    print(x)
    print(f'{"NOME":<15}{"IDADE":<10}{"SEXO":<10}')
    for info in feminino:
      print(f'{info["nome"]:<15}{info["idade"]:<10}{info["sexo"]:<10}')
  if len(masculino):
    x = 'Lista dos alunos'
    print('-' * len(x))
    print(x)
    print(f'{"NOME":<15}{"IDADE":<10}{"SEXO":<10}')   
    for info in masculino:
      print(f'{info["nome"]:<15}{info["idade"]:<10}{info["sexo"]:<10}')

print("""------------------------------
----------- ALUNOS -----------
------------------------------
""")

feminino = []
masculino = []
lista = []
dados = dict()
comando = ''

while comando.upper() != 'SAIR':
  comando = input('\nInforme o comando (novo, consulta, lista, sair): ').upper()

  if comando == 'NOVO':
    dados['nome'] = input('\nInforme o nome: ').title()
    dados['idade'] = int(input('Informe a idade: '))
    dados['sexo'] = input('Informe o sexo: ').title()

    lista.append(dados.copy())

  if comando == 'CONSULTA':
    dados = {
      'nome' : dados['nome'],
      'idade' : dados['idade'],
      'sexo' : dados['sexo']
    }
    nome = input('Informe o nome: ').title()
    if nome in dados['nome']:
      print(f'\n{"NOME":<15}{"IDADE":<10}{"SEXO":<10}')
      print(f'{dados["nome"]:<15}{dados["idade"]:<10}{dados["sexo"]:<10}')
    else:
      print('Não encontrado(a)')
  
  if comando == 'LISTA':
    lista_alf = sorted(lista, key=lambda x: x['nome'])
    filtrar_sexo(dados)
    mostrar_alunos(feminino, masculino)