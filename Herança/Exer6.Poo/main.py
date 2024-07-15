from Funcionario import Funcionario
from Vendedor import Vendedor
from Gerente import Gerente


colaborador = Vendedor(nome="João", matricula=1234, salario=3000,)
colaborador.bater_ponto(presenca=1)
print(f"{colaborador.nome} bateu a meta")

colaborador = Gerente("wendril",1234,4500,1234)
colaborador.alterar_senha(4321)
print(f"Nova senha do gerente {colaborador.nome}: {colaborador.senha}")