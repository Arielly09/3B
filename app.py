import os

print ("""Sabor Express
       """)

print('1. Cadastrar restaurante')
print('2.Listar restaurante')
print('3.Ativar restaurante')
print('4.Sair')

opcao_escolhida=int(input('Escolha uma opção:'))

def finalizar_app():
    os.system('clear')
    print('Encerrando o programa\n')

if opcao_escolhida ==1:
     print('Cadatrar restaurante')
elif opcao_escolhida ==2:
      print('Listar restaurante')
elif opcao_escolhida == 3:
      print('Ativa restaurante')
else: 
     finalizar_app()