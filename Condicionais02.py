dados = [10, 20, 30, 10]
print("=== Sistemas de Colete de Dados ===")
print("1 - Mostrar os dados")
print("2 - Alterar um dado")
print("3 - Coletar novo dado (adicionar)")
print("4 - Somar os dados")
print("5 - Localizar um dado")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
   print("Dados atuais:", dados)

elif opcao == 2:
   indice = int(input("Qual posição deseja alterar (0 a 3)?"))  
   novo_valor = int(input("Novo valor: "))
   dados[indice] = novo_valor
   print("Novo dado adicionado", dados)

elif opcao == 3:
   novo_dado = int(input("Digite o novo dado: "))
   dados.append(novo_dado)
   print("novo dado adicionado:", dados)

elif opcao == 4:
  soma = sum(dados)
  print("A soma dos dados é:", soma)

elif opcao == 5:
  procurar = int(input("Digite o valor que deseja localizar: "))
  if procurar in dados:
     print("valor não encontrado.")

else:
   print("Opção inválida.")