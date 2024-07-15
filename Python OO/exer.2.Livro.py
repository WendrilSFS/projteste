class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterareditora(self):
        print(f"editora: {self.editora}")
        novaeditora = input("digite o nome da nova editora: ")
        self.editora = novaeditora
        print(f"editora: {self.editora}")
        

    def mostrarpaginas(self):
        print(f"{self.paginas} paginas")

livroo = Livro("a lua","kaua joao","Deus na causa",250)
livroo.alterareditora()
livroo.mostrarpaginas()