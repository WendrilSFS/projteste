from Hamburger import Hamburger

# interface do usuario
codigo=int(input("Digite o codigo do produto: "))
preco=float(input("Digite o preço do produto: "))

lista=['BACON','PAO','SALADA','HAMBURGUER']

#MÉTODO DE CLASSE -> FUNÇÃO /AÇÃO
#CLASSE -> ESTRUTUTRA
#OBJETO -> VARIAVEL NO SISTEMA QUE TEM OS MOLDES
#ATRIBUTOS -> SÃO COMO UMA VARIAVEL DA CLASSE, VOCE PODE ALTERAR OS DADOS

xbacon=Hamburger(codigo,preco,lista)

preco=xbacon.getPreco()
print("Preço do xBacon: ", preco)

xbacon.getIngredientes()
xbacon.setPreco()
xbacon.setPreco()
print(xbacon.preco)