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
        

class Bateria(object):
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

        self.keyword1 = 'bateria para ' + self.nome
        self.keyword2 = 'bateria do ' + self.nome
        self.keyword3 = 'bateria ' + self.nome
        self.keyword4 = 'bateria notebook ' + self.nome
        self.campanha = str(date.today())
        self.desc = 'Bateria ' + self.nome + ' com garantia de 6 meses, 6x sem juros'

class Fonte(object):
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

        self.keyword1 = 'fonte para ' + self.nome
        self.keyword2 = 'fonte do ' + self.nome
        self.keyword3 = 'fonte ' + self.nome
        self.keyword4 = 'carregador ' + self.nome
        self.campanha = str(date.today())
        self.desc = 'Fonte ' + self.nome + ' com garantia de 6 meses, 6x sem juros'

class Tela(object):
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

        self.keyword1 = 'tela para ' + self.nome
        self.keyword2 = 'tela do ' + self.nome
        self.keyword3 = 'tela ' + self.nome
        self.keyword4 = 'tela notebook ' + self.nome
        self.campanha = str(date.today())
        self.desc = 'Tela ' + self.nome + ' com garantia de 1 ano, 6x sem juros'

        

        
