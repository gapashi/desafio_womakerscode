# Exercicios do DESAFIO do Bootcamp de Python do WoMakersCode
# -------------------------------------------------------------------------------------------------------------------------------------

# 1 - Crie um programa que solicita ao usuário que insira três notas (valores de 0 a 10) e, em seguida, calcule e exiba a média dessas notas.
# Além disso, informe ao usuário se ele foi aprovado ou reprovado com base na média das notas, considerando a média mínima de aprovação como 6.

nota1 = float(input('Digite a primeira nota: '))
if not (0 <= nota1 <= 10):
    print('ERRO! Digite um valor entre 0 e 10.')
    exit()

nota2 = float(input('Digite a segunda nota: '))
if not (0 <= nota2 <= 10):
    print('ERRO! Digite um valor entre 0 e 10.')
    exit()

nota3 = float(input('Digite a terceira nota: '))
if not (0 <= nota3 <= 10):
    print('ERRO! Digite um valor entre 0 e 10.')
    exit()

media = (nota1 + nota2 + nota3) / 3

if media < 6:
    print(f'Sua média é de {media:.2f} e infelizmente não atingiu o valor mínimo para aprovação. Você está reprovado(a)')
else:
    print(f'Sua média é de {media:.2f} e felizmente atingiu ou passou o valor mínimo para aprovação. Você foi aprovado(a)')

# 2 - Crie um programa que solicita ao usuário que insira um número inteiro e, em seguida, verifica se o número é par ou ímpar.
# O programa deve exibir uma mensagem indicando se o número é par ou ímpar.

num_int = int(input('Digite um número inteiro, sem vírgulas: '))

if not num_int % 2 == 0:
    print(f'O número {num_int} é um número ímpar.')
else:
    print(f'O número {num_int} é um número par.')

# 3 - Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo ou não.
# (Um palíndromo é uma palavra que é lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.)

def verificar_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")

    return palavra == palavra[::-1]

palavra = input("Digite uma palavra e verifique se é um palíndromo: ")
if verificar_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

# 4 - Crie um programa que solicita ao usuário que insira um número inteiro positivo e, em seguida, calcula e exibe o fatorial desse número.
# (O fatorial de um número é o produto de todos os números inteiros positivos de 1 até o próprio número.)

def calcular_fatorial(numero):

  if numero < 0:
    raise ValueError("O número deve ser positivo!")

  fatorial = 1
  for i in range(1, numero + 1):
    fatorial *= i

  return fatorial

while True:
  try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero >= 0:
      break
    else:
      print("Erro: o número deve ser positivo!")
  except ValueError:
    print("Entrada inválida. Digite um número inteiro.")

resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")

# 5 - Crie um programa que permita ao usuário gerenciar suas tarefas diárias. O programa deve oferecer as seguintes funcionalidades:
# Adicionar uma nova tarefa;
# Visualizar todas as tarefas;
# Marcar uma tarefa como concluída;
# Remover uma tarefa;
# Sair do programa.
# (Você pode implementar essas funcionalidades usando listas para armazenar as tarefas e estruturas de controle como loops e
#  condicionais para interagir com o usuário.)

import os
import datetime

tarefas = [{'titulo','data da criação','texto da tarefa','concluida':False}]

def titulo_app():
    print( """ MINHAS TAREFAS """)

def exibir_opcoes():
    print('1 - Adicionar nova tarefa')
    print('2 - Visualizar minhas tarefas')
    print('3 - Remover uma tarefa')
    print('4 - Marcar tarefa como concluída')
    print('5 - Sair\n')

def sair_app():
    exibir_subtitulo('Finalizando...')

def voltar_menu():
    input('\nAperte X para voltar ao menu principal.')
    main()

def opcao_invalida():
    print('Opção inválida. Volte ao menu principal apertando X')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '¬' * (len(texto) + 4)
    print(texto)
    print(linha)
    print()

def adicionar_tarefa():
    exibir_subtitulo('Adicionar nova tarefa')
    titulo_da_tarefa = input('Título do bloco: ')
    data_da_tarefa = datetime.datetime.now()
    texto_da_tarefa = input('Digite aqui a sua tarefa:')
    dados_da_tarefa = {'titulo':titulo_da_tarefa, 'data da criação': data_da_tarefa, 'texto da tarefa':texto_da_tarefa}
    tarefas.append(dados_da_tarefa)
    voltar_menu()

def visualizar_tarefas():
    exibir_subtitulo('Aqui estão todas as suas tarefas:\n')
    print(f'{'Título'.ljust(22)} | {'Texto'.ljust(20)} | {'Concluída'.ljust(20)}')
    for tarefa in tarefas:
        titulo_tarefa = tarefa['titulo']
        texto = tarefa['texto da tarefa']
        concluida = 'concluída' if tarefa['concluida'] else 'por fazer'
        print(f'+ {titulo_tarefa.ljust(20)} | {texto.ljust(20)} | {concluida}')
    voltar_menu()

def remover_tarefa():
    exibir_subtitulo('Remover tarefa')
    titulo_tarefa_remover = input('Digite o título  da tarefa que deseja remover: ')

    tarefa_encontrada = False
    for tarefa in tarefas:
        if tarefa['titulo'] == titulo_tarefa_remover:
            tarefas.remove(tarefa)
            tarefa_encontrada = True
            print(f'A tarefa "{titulo_tarefa_remover}" foi removida com sucesso!')
            break

    if not tarefa_encontrada:
        print(f'Tarefa "{titulo_tarefa_remover}" não encontrada.')
    voltar_menu()

def marcar_concluida():
    exibir_subtitulo('Marcar tarefa como concluída')
    titulo_tarefa = input('Qual tarefa deseja marcar como concluída? Digite o nome: ')
    tarefa_encontrada = False

    for tarefa in tarefas:
        if titulo_tarefa == tarefa['titulo']:
            tarefa_encontrada = True
            tarefa['concluida'] = not tarefa['concluida']
            mensagem = f'A tarefa {titulo_tarefa} foi concluída com sucesso!' if tarefa['concluida'] else f'A tarefa {titulo_tarefa} já foi concluída!'
            print(mensagem)
    if not tarefa_encontrada:
        print('Tarefa não encontrada.')
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            adicionar_tarefa()
        elif opcao_escolhida == 2:
            visualizar_tarefas()
        elif opcao_escolhida == 3:
            remover_tarefa()
        elif opcao_escolhida == 4:
            marcar_concluida()
        elif opcao_escolhida == 5:
            sair_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    titulo_app()
    exibir_opcoes()

if __name__ == '__main__':
    main()