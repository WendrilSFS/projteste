from Ingresso import Ingresso

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, openbar, openfood, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.openbar = openbar
        self.openfood = openfood
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.openbar:
            return "Você pode pegar uma bebida"
        else:
            return "Não há open bar neste ingresso."

    def acessar_camarote(self):
        if self.camarote:
            return "Você tem acesso ao camarote"
        else:
            return "Este ingresso não inclui acesso ao camarote."
        
preco = 50
setor = "C"
camarote = "nao incluso"
openbar = "incluso"
openfood = "incluso"
estacionamento = "incluso"


vip = IngressoVIP(preco,setor,camarote,openbar,openfood,estacionamento) 
print(vip.pegar_bebida())   
print(vip.acessar_camarote()) 
    