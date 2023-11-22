import unittest
from biblioteca import Biblioteca
from livro import Livro

class TestBiblioteca(unittest.TestCase):

    def test_buscar_livro_existente(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 863)
        livro = biblioteca.buscar_livro("Dom Quixote", "Miguel de Cervantes")
        self.assertIsNotNone(livro)

    def test_buscar_livro_inexistente(self):
        biblioteca = Biblioteca()
        livro = biblioteca.buscar_livro("Harry Potter", "J.K. Rowling")
        self.assertIsNone(livro)

    def test_empresta_livro_disponivel(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 863)
        resultado = biblioteca.empresta_livro("Dom Quixote", "Miguel de Cervantes")
        self.assertEqual(resultado, "Empréstimo realizado com sucesso")

    def test_empresta_livro_indisponivel(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 863)
        biblioteca.empresta_livro("Dom Quixote", "Miguel de Cervantes")
        resultado = biblioteca.empresta_livro("Dom Quixote", "Miguel de Cervantes")
        self.assertEqual(resultado, "Livro indisponível")

    def test_maior_livro(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 863)
        biblioteca.adicionar_livro("Harry Potter", "J.K. Rowling", 500)
        biblioteca.adicionar_livro("1984", "George Orwell", 328)

        maior = biblioteca.maior_livro()
        self.assertEqual(maior, 863)  # Verifica se o maior número de páginas é 863 (Dom Quixote)

    def test_menor_livro(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 863)
        biblioteca.adicionar_livro("Harry Potter", "J.K. Rowling", 500)
        biblioteca.adicionar_livro("1984", "George Orwell", 328)

        menor = biblioteca.menor_livro()
        self.assertEqual(menor, 328)  # Verifica se o menor número de páginas é 328 (1984)

if __name__ == '__main__':
    unittest.main()
