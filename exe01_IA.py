#Sistema Simplificado de Streaming de Vídeo

#Criar uma lista de vídeos
filmes = ['lua', 'sol']
series = ['yin', 'yang']

"""
Foi criado uma função para exibir todos os itens de cada lista,
utilizou-se o loop -for- para processar a lista de filmes e de séries
"""
def catalogo(filmes, series):
    print("===================")
    print("Catálogo de filmes:")
    for listar_filmes in filmes:
        print(listar_filmes)

    print("Catálogo de séries:")
    for listar_series in series:
        print(listar_series)
    print("===================")

'''
-> A função  abaixo tem como objetivo exibir o catálogo e permitir que o usuário escolha o que deseja assistir entre as opções;
-> Após chamar a função de catálogo um contador foi adicionado para ser usado como condição do laço de repetição -while-;
-> O -input- permite ao sistema interagir com o usuário e dependendo da entrada a função condicional -if e else- responderá;
-> Enquanto o usuário digitar filmes fora do catálogo o sistema permitirá uma nova escolha.
'''
def iniciar_streaming(self):
    catalogo(filmes, series)
    count = 1
    while count > 0:
        escolha = input('Digite o nome do filme ou série que deseja assistir: ')
        if escolha in filmes or escolha in series:
            print('\n         **********************')
            print('           iniciando', {escolha})
            print('         **********************\n')
            count = 0
        else:
            print('\n**********************************************')
            print('Este filme ou série ainda não está disponível.')
            print('    Escolha entre as nossas outras opções!')
            print('**********************************************\n')
      
#Chamando a função iniciadora do sistema
iniciar_streaming(catalogo)
