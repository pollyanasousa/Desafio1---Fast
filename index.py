# Adicionar um novo registro de estudante (nome, ID e notas).
atendimento = True
outroAtendimento = True
d = {}
lista = []
contador = 0
soma = 0
media = 0

saudacao = "Olá, seja bem vindo(a)!"
print(saudacao)

while atendimento == True or outroAtendimento == "sim":

  atendimento = input("Por favor digite a opção desejada: \n 1 - Cadastro de estudante; \n 2 - Consultar registros de estudantes; \n 3 - Consultar estudante pelo seu ID; \n 4 - Consultar média de notas de todos os estudantes; \n 5 - Salvar registros de estudantes em um arquivo; \n 6 - Carregar os registros de estudantes de um arquivo; \n 7 - Sair. \n")
  
  if atendimento == "1": 
     contador += 1
     d["id"] = contador
     d["nome"] = input(" Ok!Por favor, digite o nome do estudante: ")
     d["notas"] = (input("Informe a nota do estudante: "))
     lista.append(d.copy())   
     resposta = input("Deseja cadastrar novo estudante, digite sim ou nao: ") 

     while resposta == "sim":
       contador += 1
       d["id"] = contador
       d["nome"] = input(" Ok!Por favor, digite o nome do estudante: ")
       d["notas"] = (input("Informe a nota do estudante: "))
       lista.append(d.copy())
       resposta = input("Cadastrar novo estudante, digite sim ou nao: ") 

       if resposta == "nao":
         print("Estudante(s) cadastrado(a)s com sucesso!") 
         outroAtendimento = input("Deseja outro atendimento, digite sim ou nao? ")
                 
        # 2 - Exibir uma lista de todos os registros de estudantes.
  elif atendimento == "2":
    if len(lista) == 0:
      print("Sem registros!")
    for p in lista:
      print(f"Todos registros: \n {p}\n")
    outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao? ")
    if outroAtendimento == "nao":
      print("Fim do atendimento, até logo!")
        
      #  3 - Procurar um estudante pelo seu ID e exibir seu registro.
  elif atendimento == "3":
      if len(lista) == 0:
       print("Sem registro!")
       outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
       if outroAtendimento == "nao":
        print("Fim do atendimento, até logo!")
        break
      estudanteId = int(input("Por favor, para o buscar os dados do estudante desejado, digite o id: "))
      for p in lista:
        if p["id"] == estudanteId:
          print(f"O(a) estudante é {p}")        
          outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao? ")       
          if outroAtendimento == "nao":
           print("Fim do atendimento, até logo!")   
      
  elif atendimento == "4":
    if len(lista) == 0:
      print("Sem registro!")
      outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
      if outroAtendimento == "nao":
        print("Fim do atendimento, até logo!")
    else: 
     for p in lista:
       soma += int(p["notas"])
       media +=1
       resultado = soma / media   
     print(f"A média das notas dos estudantes é {resultado}")
     outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
     if outroAtendimento == "nao":
      print("Fim do atendimento, até logo!")

      # Salvar os registros de estudantes em um arquivo de texto
  elif atendimento == "5":
    if len(lista) == 0:
      print("Sem registro!")
      outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
      if outroAtendimento == "nao":
       print("Fim do atendimento, até logo!")
    else: 
      for p in lista:
       arquivo = str(p)  
       print("Registros salvos com sucesso!")   
      outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
      if outroAtendimento == "nao":
       print("Fim do atendimento, até logo!")

    # Carregar os registros de estudantes de um arquivo de texto     
  elif atendimento == "6":
    if len(lista) == 0:
      print("Sem registro!")
      outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
      if outroAtendimento == "nao":
        print("Fim do atendimento, até logo!")
    else:   
     print(f"Alunos cadastrados {arquivo}")
     outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
     if outroAtendimento == "nao":
      print("Fim do atendimento, até logo!")

  elif atendimento == "7":
    print("Fim do atendimento, até logo!")
    break

  else:
    print("Desculpa, não entendi.")
    outroAtendimento = input("Deseja continuar com atendimento, digite sim ou nao?")
    if outroAtendimento == "nao":
      print("Fim do atendimento, até logo!")
