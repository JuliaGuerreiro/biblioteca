from livro import Livro

class Biblioteca:

  def __init__(self):
    self.livros = []

  def adicionar_livro(self, titulo, autor, paginas):
    if self.buscar_livro(titulo, autor) is None:    
      livro = Livro()
      livro.titulo = titulo
      livro.autor = autor
      livro.paginas = paginas
      self.livros.append(livro)
    else:
      print("Livro já cadastrado")

  def buscar_livro(self, titulo, autor):
    for livro in self.livros:
      if livro.titulo == titulo and livro.autor == autor:
        return livro
    return None

  def empresta_livro(self, titulo, autor):
    livro = self.buscar_livro(titulo, autor)
    if livro is not None:
        if livro.disponivel:
            livro.disponivel = False
            return "Empréstimo realizado com sucesso"
        else:
            return "Livro indisponível"
    else:
        return "Livro não encontrado"

  def devolve_livro(self, titulo, autor):
    livro = self.buscar_livro(titulo, autor)
    if livro is not None:
        if not livro.disponivel:
            livro.disponivel = True
            print("Devolução realizada com sucesso")
        else:
            print("Livro já está disponível")
    else:
        print("Livro não encontrado")
    
  def maior_livro(self):
    maior = 0
    livro = None
    for livro in self.livros:
      if livro.paginas > maior:
        maior = livro.paginas
    return maior

  def menor_livro(self):
    menor = 1000000
    livro = None
    for livro in self.livros:
      if livro.paginas < menor:
        menor = livro.paginas
    return menor

  def lista_livros(self):
    for livro in self.livros:
      print(f"Título: {livro.titulo}, Autor: {livro.autor}")

  def lista_emprestados(self):
    livros_emprestados = []  
    for livro in self.livros:
        if not livro.disponivel:
            livros_emprestados.append(f"Título: {livro.titulo}, Autor: {livro.autor}")
    return livros_emprestados  

  def lista_disponiveis(self):
    livros_disponiveis = []  
    for livro in self.livros:
        if livro.disponivel:
            livros_disponiveis.append(f"Título: {livro.titulo}, Autor: {livro.autor}")
    return livros_disponiveis  

