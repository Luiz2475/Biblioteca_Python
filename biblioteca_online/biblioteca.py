biblioteca = [
 {"titulo": "Python Básico", "autor": "João Silva", "ano": 2021, "disponivel": True},
 {"titulo": "Algoritmos Avançados", "autor": "Maria Souza", "ano": 2019, "disponivel": True},
 {"titulo": "Machine Learning", "autor": "Carlos Pereira", "ano": 2020, "disponivel": True},
 {"titulo": "Data Science", "autor": "Ana Martins", "ano": 2018, "disponivel": True},
 {"titulo": "Deep Learning", "autor": "Pedro Alves", "ano": 2022, "disponivel": True}
]

def adicionar_livro(titulo, autor, ano):
  for livro in biblioteca:
    if livro["titulo"].upper() == titulo.upper() and livro["autor"].upper() == autor.upper():
        print(f'O livro "{titulo}" de {autor} já está na biblioteca.')
        return
  novo_livro = {"titulo": titulo, "autor": autor, "ano": int(ano), "disponivel": True}
  biblioteca.append(novo_livro)
  print("------------------------------------------------")
  print(f'O livro "{titulo}" foi adicionado com sucesso!')
  print("------------------------------------------------")
  
def buscar_livro(titulo):
    buscar = titulo.upper()
    procurar = []
    for livro in biblioteca:
     if buscar in livro["titulo"].upper():
        procurar.append(livro)
    if procurar:
        print("Livros achados:")
        for livro in procurar:
            print("------------------------------------------------")
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Ano: {livro["ano"]}, Disponível: {"Sim" if livro["disponivel"] else "Não"}')
            print("------------------------------------------------")
    else:
        print("------------------------------------------------")
        print("Nenhum livro encontrado com esse título.")
        print("------------------------------------------------")

def listar_livros():
   for livro in biblioteca:
      print("------------------------------------------------")
      print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Ano: {livro["ano"]}, Disponível: {"Sim" if livro["disponivel"] else "Não"}')
      print("------------------------------------------------")
def emprestar_livro(titulo):
   for livro in biblioteca:
      if livro["titulo"].upper() == titulo.upper():
        if livro["titulo"].upper() == titulo.upper():
            if livro["disponivel"]:
                livro["disponivel"] = False
                print("------------------------------------------------")
                print(f'O livro "{titulo}" foi emprestado com sucesso.')
                print("------------------------------------------------")
            else:
                print("------------------------------------------------")
                print(f'O livro "{titulo}" não está disponível no momento.')
                print("------------------------------------------------")
            return

def devolver_livro(titulo):
   for livro in biblioteca:
    if livro["titulo"].upper() == titulo.upper():
       if not livro["disponivel"]:
                livro["disponivel"] = True
                print("------------------------------------------------")
                print(f'O livro "{titulo}" foi devolvido com sucesso.')
                print("------------------------------------------------")
       else:    
                print("------------------------------------------------")
                print(f'O livro "{titulo}" já está disponível na biblioteca.')
                print("------------------------------------------------")
       return
    
   

while True:
 obter = int(input("Bem-vindo a Biblioteca online!!! \n 1-Adicionar Livro \n 2-Buscar Livro \n 3-Listar Livros \n 4-Emprestar Livro \n 5-Devolver Livro \n 6-Sair \n Escolher opção: "))
 if obter == 1:
   titulo = input("Titulo do livro: ")
   autor  = input("Autor do livro: ")
   ano = int(input("Ano do livro: "))
   adicionar_livro(titulo, autor, ano)
 elif obter == 2:
   titulo = input("Titulo do livro: ")
   buscar_livro(titulo)
 elif obter == 3:
   listar_livros()
 elif obter == 4:
   titulo = input("Titulo do livro: ")
   emprestar_livro(titulo)
 elif obter == 5:
    titulo = input("Titulo do livro: ")
    devolver_livro(titulo)
 elif obter == 6:
    print("Obrigado pela atenção")
    break
 else:
    print("Obrigado pela atenção")
    break