
computadores = []

while True:
    print('\n--- SISTEMA DE TI ---')
    print('1 - Cadastrar computador')
    print('2 - Listar computadores')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome do computador: ')
        processador = input('Processador: ')
        memoria = input('Memória RAM: ')

        computador = {
            'nome': nome,
            'processador': processador,
            'memoria': memoria
        }

        computadores.append(computador)

        print('Computador cadastrado!')

    elif opcao == '2':
        if len(computadores) == 0:
            print('Nenhum computador cadastrado.')

        for computador in computadores:
            print('\nNome:', computador['nome'])
            print('Processador:', computador['processador'])
            print('Memória RAM:', computador['memoria'])

    elif opcao == '3':
        print('Sistema encerrado!')
        break

    else:
        print('Opção inválida!')
