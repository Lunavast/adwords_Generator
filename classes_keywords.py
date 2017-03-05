from datetime import date

class Teclado(object):
    def __init__(self,sku,marca,modelo,serie,entity,name,link):
        self.sku = sku
        self.marca = marca
        self.modelo = modelo
        self.serie = serie
        self.entity = entity
        self.name = name
        self.link = link
        if modelo != '':
            self.nome = self.marca + " " + self.modelo + " " + self.serie
        else:
            self.nome = self.marca + " " + self.serie

        self.keyword1 = 'teclado para ' + self.nome
        self.keyword2 = 'teclado do ' + self.nome
        self.keyword3 = 'teclado ' + self.nome
        self.keyword4 = 'teclado notebook ' + self.nome
        self.campanha = str(date.today())
        self.desc = 'Teclado ' + self.nome + ' com garantia de 1 ano, 6x sem juros'
