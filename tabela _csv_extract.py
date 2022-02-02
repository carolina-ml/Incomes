# ler uma tabela csv em que as colunas sejam o nome dos dados da conta corrente, 
# uma coluna com a entrada de grana, outra com saída
# e um cálculo com variação que sofre mensalmente

import csv

def build(saldo):

        valor_do_saldo = {}

#specify that the file should be handled as text mode

    with open('finances_csv.csv', 'rt') as ficheiro_total:
        for linha in csv.Reader(ficheiro_total):
            reader = csv.reader(ficheiro)
            valor_do_saldo[row['débito']] = row['data']
            
#balance the variation between months            
            
    mês_corrente = int(valor_do_saldo['mês-corrente--'])
    valor_do_saldo['-mês-anterior--'] = str(mês_corrente + 1)
    valor_do_saldo['-mês-anterior--'] = str(mês_corrente - 1)
    valor_do_saldo['-três-últimos-meses--'] = f'{str(mês_corrente - 3)}, {str(mês_corrente - 2)} e {str(mês_corrente - 1)}'
    valor_do_saldo['-data-ínicio--'] = f'01 de {mês_corrente'}'

    for tipo_de_gasto in saldo:
        with open(f'./extrato/{tipo_de_gasto}/finances.readlines', 'r') as debt:
            valor = debt.read()
            
            for i in valor_do_saldo:
                valor = credit.replace(i, valor_do_saldo)
                
        with open(f' ./extrato/{tipo_de_gasto}/finances.readlines, 'w') as teste:
            teste.write(valor)

return valor_do_saldo



