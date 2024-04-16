import os

restaurantes = ['Pizza','Xp']

def exibir_npme_do_programa():
 print ("""
       Paula Tejano
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



def exibir_subtitulo(texto):
    os.system('clear')
    linha='*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Digite o novos restaurantes:')
    categoria = input('Digite a categoria do restaurante{nome_do_restaurante:} ')
    dado_do_restaurante ={"nome":nome_do_restaurante,'categoria':categoria,'ativo':False}
    nome_do_restaurante = input(f"Digite o nobo nome do restaurante {nome_do_restaurante}: ")
    print(f'Orstaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    restaurantes.append(dado_do_restaurante)
    print(f'O restaurante {nome_do_restaurante}foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    
def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes')
    
    print(f'{"nome do restaurante".ljust(22)}  |  {"categoria"ljust(22)  |  status}'  )
    for restaurante in restaurantes:
        nome_restaurante =['no,e']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurantes['ativos'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)}  |  {categoria.ljust(20)  |  {ativo}}')
        
        voltar_ao_menu_principal()


def opcao_invalida():
    print('opção invalida!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        print(f'*{restaurante}')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()
def cadastro_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes: ')
    nome_restaurante = input('Digite o nome do novo restaurante')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante{nome_restaurante}foi cadastrado com sucesso!')
    voltar_ao_menu_principal() 
    
def escolher_opcao():
 try:

    opcao_escolhida = int(input('Escolha uma opção'))

    if opcao_escolhida == 1:
        cadastro_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurante()
    elif opcao_escolhida == 3:
        print('Ativa restaurante')
    elif opcao_escolhida == 4:        
        finalizar_app()
    else:
       opcao_invalida() 
 except:
      opcao_invalida()
      
def main():
         os.system('clear')
         exibir_npme_do_programa()
         exibir_opcoes()
         escolher_opcao()

if __name__== '__main__':
    main()
