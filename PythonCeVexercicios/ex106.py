# MINI SISTEMA INTERACTIVE HELP #

def ajuda(com):
    help(com)

comando = ''
while True:
    comando = input('Função ou BIBLIOTECA: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)