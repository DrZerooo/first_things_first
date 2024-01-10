saldo = 1000.00
op = True

while op == True:

    action = int( input('''Escolha uma ação: 
                    1 - consultar saldo
                    2 - depositar
                    3 - sacar
                    0 - finalizar operação
                    Digite o número da ação: '''))

    if action == 1:
        print('Seu saldo é de R$', saldo)
    elif action == 2:
        deposito = float( input( "Digite o valor a ser depositado: R$"))
        saldo = saldo + deposito
    elif action == 3:
        saque = float( input( "Digite o valor a ser sacado: R$"))
        if saque > saldo:
            print('ERRO! Saldo insuficiente!')
        else:
            saldo = saldo - saque
    else:
        op = False

print( 'Operação finalizada!')