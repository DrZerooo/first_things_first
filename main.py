pessoa = {
    'Nome' : 'Bruno',
    'Sobrenome' : 'Picanha',
    'Idade' : '82'
}

# print(pessoa['Sobrenome'])

# for chave in pessoa:
#     print (chave, '=', pessoa[chave]) 

for chave, valor in pessoa.items():
    print(f'{chave} = {valor}')