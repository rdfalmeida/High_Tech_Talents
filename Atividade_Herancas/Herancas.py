#Fazer a herança das seguintes classes:
#MeioTransporte
#Terrestre            / Aquatico           / Aereo
#Carro / Caminhao     Remo / Barco       Avião / Helicóptero
#Use a imaginação para criar e separar os seus atributos
#Para o dia 07/04


class MeioTransporte:
    'General class for all means of transportation'
    
    def __init__(self, idnumber, cor):
        self.idnumber = idnumber
        self.cor = cor
        
    def login(self):
        print('Insira seu nome: ')
        username = input()
        print('Oi, {}. Seja bem vindo!'.format(username))

class Terrestre(MeioTransporte):
    'General Class for all land transportations'
    
    def __init__(self, idnumber, cor, rodas, portas):
        super().__init__(idnumber, cor)
        self.rodas = rodas
        self.portas = portas

class Carro(Terrestre):
    'Class for cars'

    def __init__(self, idnumber, cor, rodas, portas, consumo):
        super().__init__(idnumber, cor, rodas, portas)
        self.consumo = consumo

class Caminhao(Terrestre):
    'Class for trucks'

    def __init__(self, idnumber, cor, rodas, portas, carga):
        super().__init__(idnumber, cor, rodas, portas)
        self.carga = carga

class Aquatico(MeioTransporte):
    'General Class for all aquatic transportations'

    def __init__(self, idnumber, cor, velas, pes):
        super().__init__(idnumber, cor)
        self.velas = velas
        self.pes = pes

class Remo(Aquatico):
    'Class for rowboats'

    def __init__(self, idnumber, cor, velas, pes, quantidaderemos):
        super().__init__(idnumber, cor, velas, pes)
        self.quantidaderemos = quantidaderemos

class Barco(Aquatico):
    'Class for motorized boats'
    def __init__(self, idnumber, cor, velas, pes, potenciamotor):
        super().__init__(idnumber, cor, velas, pes)
        self.potenciamotor = potenciamotor

class Aereo(MeioTransporte):
    'General Class for all aerial transportations'

    def __init__(self, idnumber, cor, fuselagem, autonomia):
        super().__init__(idnumber, cor)
        self.fuselagem = fuselagem
        self.autonomia = autonomia

class Aviao(Aereo):
    'Class for areroplanes'

    def __init__(self, idnumber, cor, fuselagem, autonomia, quantidade_passageiros):
        super().__init__(idnumber, cor, fuselagem, autonomia)
        self.quantidade_passageiros = quantidade_passageiros

class Helicoptero(Aereo):
    'Class for helicopters'

    def __init__(self, idnumber, cor, fuselagem, autonomia, tipo_helice):
        super().__init__(idnumber, cor, fuselagem, autonomia)
        self.tipo_helice = tipo_helice


car = Carro('007', 'branco', '4', '4', '12')
hc = Helicoptero('001', 'azul', 'metal', '300km', 'inclinada')
boat = Barco('003', 'dourado', '3', '90', 'undefined')
car.login()

#Aqui vão os testes básicos:
print('Helicóptero ID {}\nCor: {}, Tipo de fuselagem: {}'.format(hc.idnumber, hc.cor, hc.fuselagem))
print('Autonomia: {}, Tipo de Hélice: {}\n'.format(hc.autonomia, hc.tipo_helice))
print(car.idnumber, car.cor, car.rodas, car.portas, car.consumo)
print(boat.idnumber, boat.cor, boat.velas, boat.pes, boat.potenciamotor)