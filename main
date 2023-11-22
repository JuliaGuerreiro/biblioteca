from biblioteca import Biblioteca
from livro import Livro

def main():
  biblioteca = Biblioteca()

  biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 863)
  biblioteca.adicionar_livro("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 320)
  biblioteca.adicionar_livro("1984", "George Orwell", 328)

  # Cadastrar livro na biblioteca
  biblioteca.adicionar_livro("A Brief History of Time", "Stephen Hawking", 256)

  # Emprestar livros
  result1 = biblioteca.empresta_livro("A Brief History of Time", "Stephen Hawking")
  result2 = biblioteca.empresta_livro("Harry Potter and the Philosopher's Stone", "J.K. Rowling")

  print(result1)
  print(result2)

  # Devolver um livro
  biblioteca.devolve_livro("A Brief History of Time", "Stephen Hawking")

  # Mostrar livros emprestados
  emprestados = biblioteca.lista_emprestados()
  for livro in emprestados:
      print(livro)

  # Mostrar livros disponíveis
  disponiveis = biblioteca.lista_disponiveis()
  for livro in disponiveis:
      print(livro)
  
  # Mostrar livro com o maior número de páginas
  print(biblioteca.maior_livro())

  # Mostrar livro com o menor número de páginas
  print(biblioteca.menor_livro())
  
main()

