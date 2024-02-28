#Sistema de Sistema Simplificado de Streaming de Vídeo

filmes = ['lua', 'sol']
series = ['yin', 'yang']

def catalogo(filmes, series):
    print("===================")
    print("Catálogo de filmes:")
    for listar_filmes in filmes:
        print(listar_filmes)

    print("Catálogo de séries:")
    for listar_series in series:
        print(listar_series)
    print("===================")

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
      

iniciar_streaming(catalogo)