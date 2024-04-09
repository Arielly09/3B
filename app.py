import os

restaurante = ['Pizza','Xp']

def exibir_npme_do_programa():
 print ("""Paula Tejano
       """)
def exibir_opcoes():
 print('1. Cadastrar restaurante')
 print('2.Listar restaurante')
 print('3.Ativar restaurante')
 print('4.Sair')

def finalizar_app():
   exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    input('\n Digite a tecla "Enter"para voltar ao menu principal')
    main()

opcao_escolhida=int(input('Escolha uma opção:'))
def exibir_subtitulo(texto):
    os.system('clear')
    print('texto')
    print()

def escolher_opcao():
 
      if opcao_escolhida ==1:
            print('Cadatrar restaurante')
      elif opcao_escolhida ==2:
            print('Listar restaurante')
      elif opcao_escolhida == 3:
            print('Ativa restaurante')
      else: 
            finalizar_app()

def main():
         os.system('clear')
         exibir_npme_do_programa()
         exibir_opcoes()
         escolher_opcao()

if __name__== '__main__':
    main()
