dados  =  {'login':[], 'senha':[]}
produtos = {'camisa': 60, 'tenis': 130, 'calça': 90}

login = input ("Crie um login: ")
senha = input ("Crie uma senha:")

dados['login'].append(login)
dados['senha'].append(senha)

print("\nProdutos disponiveis:")
print("camisa - R$60")
print("tenis - R$130")
print("calça - R$90")

escolha = input ("\nQual produto deseja comprar?")

if escolha in produtos: 
    valor_total = produtos[escolha]
    print(f"\nVoce escolheu {escolha} que custa R${valor_total}")
    pagar = input ("Deseja pagar? (s\n): ")

    if pagar == 's':
        print("pagamento realizado com sucesso!.")
    else:
        print("Compra cancelada!.")
else:
    print("Compra não encontrada.")

