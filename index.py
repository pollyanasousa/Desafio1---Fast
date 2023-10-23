# Adicionar um novo registro de estudante (nome, ID e notas).
atendimento = True
d = {}
lista = []
contador = 0

saudacao = "Olá, seja bem vindo(a)!"
print(saudacao)

while atendimento == True or outroAtendimento == "sim":

  atendimento = input("Por favor digite a opção desejada: \n 1 - Cadastro de estudante; \n 2 - Consutar registros de estudantes; \n 3 - Consultar estudante pelo seu ID; \n 4 - Consultar média de notas de todos os estudantes; \n 5 - Salvar registros de estudantes em um arquivo; \n 6 - Carregar os registros de estudantes de um arquivo; \n 7 - Sair. \n")
  
  if atendimento == "1": 
     contador += 1
     d["id"] = contador
     d["nome"] = input(" Ok!Por favor, digite o nome do estudante: ")
     d["notas"] = (input("Informe a nota do estudante: "))
     lista.append(d.copy())   
     resposta = input("Deseja continuar, digite sim ou nao: ") 

     while resposta == "sim":
       contador += 1
       d["id"] = contador
       d["nome"] = input(" Ok!Por favor, digite o nome do estudante: ")
       d["notas"] = (input("Informe a nota do estudante: "))
       lista.append(d.copy())
       resposta = input("Deseja continuar, digite sim ou nao: ") 

       if resposta == "nao":
         print("Estudante cadastrado com sucesso!") 
         outroAtendimento = input("Deseja outro atendimento, digite sim ou nao? ")
         print(outroAtendimento)
        
        # 2 - Exibir uma lista de todos os registros de estudantes.
  elif atendimento == "2":
    print(f"A lista de todos os registros de estudantes cadastrados é\n{lista}")
    resposta = input("Deseja continuar, digite sim ou nao: ") 
    if resposta == "nao":
        outroAtendimento = input("Deseja outro atendimento, digite sim ou nao? ")
        print(outroAtendimento)
      #  3 - Procurar um estudante pelo seu ID e exibir seu registro.
  elif atendimento == "3":
       estudanteId = int(input("Por favor, para o buscar os dados do estudante desejado, digite o id: "))
       for p in lista:
        if p["id"] == estudanteId:
          print("O estudantes é ", p["nome"] + " com notas", p["notas"])
        
       outroAtendimento = input("Deseja outro atendimento, digite sim ou nao? ")        
      
  elif atendimento == "4":
    print("opção 4")
    


    
    





    


      
    

        
   



        


  


# alunos = {}

# alunos["nome"] = input("Digite o nome do aluno: ")
# alunos["notas1"] = float("Digite sua primeira nota: ")
# alunos["notas2"] = float("Digite sua segunda nota: ")
# alunos["notas3"] = float("Digite sua terceira nota: ")
# alunos["notas4"] = float("Digite sua quarta e ultima nota: ")
# print(alunos)