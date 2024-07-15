class Livro:
    def __init__(self,nome:str,autor:str,editora:str,pags:int):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = pags

    def getpaginas(self):
        print(self.paginas)

    def seteditora(self,novaeditora):
        self.editora = novaeditora


livro1 = Livro("jao pe de feijao","jao","seila","235")

livro1.getpaginas()

print(livro1.editora)

livro1.seteditora("seila2")

print(livro1.editora)