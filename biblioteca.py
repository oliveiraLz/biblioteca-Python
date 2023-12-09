class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False

    def devolver(self):
        self.disponivel = True


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            return True
        else:
            return False

    def devolver_livro(self, livro):
        livro.devolver()
        self.livros_emprestados.remove(livro)


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" cadastrado na biblioteca.')

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f'Usuário {usuario.nome} cadastrado com sucesso!')

    def listar_livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.livros if livro.disponivel]
        for livro in livros_disponiveis:
            print(f'Título: {livro.titulo}, Autor: {livro.autor}')

    def emprestar_livro(self, livro, usuario):
        if livro in self.livros and usuario in self.usuarios:
            if livro.emprestar():
                usuario.livros_emprestados.append(livro)
                print(f'Livro "{livro.titulo}" emprestado para {usuario.nome}.')
                return True
        print(f'Não foi possível emprestar o livro para {usuario.nome}.')
        return False

    def devolver_livro(self, livro, usuario):
        if livro in usuario.livros_emprestados:
            livro.devolver()
            usuario.livros_emprestados.remove(livro)
            print(f'Livro "{livro.titulo}" devolvido por {usuario.nome}.')
            return True
        print(f'Não foi possível devolver o livro por {usuario.nome}.')
        return False


## definindo as variáveis livros

# livro1 = Livro("Aprendendo Python", "John Smith")
# livro2 = Livro("Introdução à POO", "Alice Johnson")
# livro3 = Livro("Livro para o Raphael", "Professor de POO")

## Criação de usuário

# usuario1 = Usuario("João")
# usuario2 = Usuario("Maria")
# usuario3 = Usuario("Raphael")

## Instância de biblioteca
# biblioteca = Biblioteca()

## Cadastro de livros

# biblioteca.cadastrar_livro(livro1)
# biblioteca.cadastrar_livro(livro2)
# biblioteca.cadastrar_livro(livro3)

## Cadastro de Usuários

# biblioteca.cadastrar_usuario(usuario1)
# biblioteca.cadastrar_usuario(usuario2)
# biblioteca.cadastrar_usuario(usuario3)

## Chamada dos métodos da biblioteca

# biblioteca.listar_livros_disponiveis()
# biblioteca.emprestar_livro(livro3, usuario3)
# biblioteca.listar_livros_disponiveis()
# biblioteca.devolver_livro(livro3,usuario3)
# biblioteca.listar_livros_disponiveis()


