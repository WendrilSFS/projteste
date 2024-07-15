#Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes atributos:​Nome,Autor,Editora,Páginas​
#A classe deve ter o seguintes métodos:Alterar_editora(),Listar_qtde_paginas()​

class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome=nome
        self.autor=autor
        self.editora=editora
        self.paginas=paginas
    
    def alterarEditora(self,novaEditora):
        self.editora=novaEditora

    def listarQntdPaginas(self,novasPaginas):
        self.paginas=novasPaginas
        