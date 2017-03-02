import pymysql
import datetime
import xlwt
from classes_keywords import Teclado
from classes_keywords import Fonte
from classes_keywords import Bateria
from classes_keywords import Tela
import requests
from datetime import date

conn = pymysql.connect(host='*******',
                       port=********,
                       user='**********',
                       passwd='******')

cur = conn.cursor()

cur.execute('******')

data = str(datetime.date.today())
print ("executando query...")
cur.execute("select * from products_added_today where created_at between subdate(curdate(), interval 50 day) and subdate(curdate(), interval 3 day) limit 100")

print ("query finalizada")
x = cur.fetchall()
cur.close()
conn.close()

keyboard = []
battery = []
adapter = []
screen = []

def mini_name(name_m):
    mini = name_m.lower()
    mini = mini.replace(" ","-")
    return mini

def w_link(name_link, id_t):
    r1 = requests.get('http://www.******.com.br/' + name_link + '.html')
    if r1.status_code == 200:
        return('http://www.*******.com.br/' + name_link + '.html')
    else:
        r2 = requests.get('http://www.********.com.br/' + name_link + '-' + str(id_t) + '.html')
        if r2.status_code == 200:
            return('http://www.******.com.br/' + name_link + '-' + str(id_t) + '.html')
    
print('Verificando links...')

for result in x:
    sku, marca, modelo, serie, data, entity, name = result
    try:
        if sku[0]+sku[1] == 'TC':
            notebook = Teclado(sku,marca,modelo,serie,entity,mini_name(name),w_link(mini_name(name),entity))
            if notebook.link is not None:
                keyboard.append(notebook)
        if sku[0]+sku[1] == 'BC':
            notebook = Bateria(sku,marca,modelo,serie,entity,mini_name(name),w_link(mini_name(name),entity))
            if notebook.link is not None:
                battery.append(notebook)
        if sku[0]+sku[1] == 'TE':
            notebook = Tela(sku,marca,modelo,serie,entity,mini_name(name),w_link(mini_name(name),entity))
            if notebook.link is not None:
                screen.append(notebook)
        if sku[0]+sku[1] == 'FT':
            notebook = Fonte(sku,marca,modelo,serie,entity,mini_name(name),w_link(mini_name(name),entity))
            if notebook.link is not None:
                adapter.append(notebook)
    except:
        print("erro no link")
        
        

all_p = [keyboard,battery,adapter,screen]

print('Gravando dados...')

#SAÍDA

#GRUPO DE ANUNCIOS

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("Grupos de anuncios")
worksheet.write(0,0,"Campaign")
worksheet.write(0,1,"Ad Group")
worksheet.write(0,2,"Max CPC")
worksheet.write(0,3,"Max CPM")
worksheet.write(0,4,"Campaign Daily Budget")
worksheet.write(0,5,"Campaign Type")
worksheet.write(0,6,"Networks")
worksheet.write(0,7,"Languages")
worksheet.write(0,8,"Bid Strategy Type")
worksheet.write(0,9,"Ad rotation")
worksheet.write(0,10,"Delivery method")
worksheet.write(0,11,"Targeting method")
worksheet.write(0,12,"Exclusion method")
worksheet.write(0,13,"Campaign Status")
#CONTEUDO FIXO
worksheet.write(1,4,"50.00")
worksheet.write(1,5,"Search Network only")
worksheet.write(1,6,"Google search;Search Partners")
worksheet.write(1,7,"pt")
worksheet.write(1,8,"Manual CPC")
worksheet.write(1,9,"Optimize for clicks")
worksheet.write(1,10,"Standard")
worksheet.write(1,11,"Location of presence or Area of interest")
worksheet.write(1,12,"Location of presence or Area of interest")
worksheet.write(1,13,"Active")




row = 1
for categoria in all_p:
    for x in categoria:
        worksheet.write(row,0,x.campanha)
        worksheet.write(row,1,x.nome)
        worksheet.write(row,2,'0.20')
        worksheet.write(row,3,'0.01')
        row = row+1

#PALAVRAS CHAVES

worksheet2 = workbook.add_sheet("Keywords")
worksheet2.write(0,0,"Campaign")
worksheet2.write(0,1,"Ad Group")
worksheet2.write(0,2,"Keyword")
worksheet2.write(0,3,"Criterion Type")

row = 1
for categoria in all_p:
    for x in categoria:
        
        worksheet2.write(row,0,x.campanha)
        worksheet2.write(row,1,x.nome)
        worksheet2.write(row,3,'Phrase')
        worksheet2.write(row+1,0,x.campanha)
        worksheet2.write(row+1,1,x.nome)
        worksheet2.write(row+1,3,'Phrase')
        worksheet2.write(row+2,0,x.campanha)
        worksheet2.write(row+2,1,x.nome)
        worksheet2.write(row+2,3,'Phrase')
        worksheet2.write(row+3,0,x.campanha)
        worksheet2.write(row+3,1,x.nome)
        worksheet2.write(row+3,3,'Phrase')
        
        worksheet2.write(row,2,x.keyword1)
        row = row+1
        worksheet2.write(row,2,x.keyword2)
        row = row+1
        worksheet2.write(row,2,x.keyword3)
        row = row+1
        worksheet2.write(row,2,x.keyword4)
        row = row+1

#ANUNCIOS

worksheet3 = workbook.add_sheet("Anuncios")
worksheet3.write(0,0,"Campaign")
worksheet3.write(0,1,"Ad Group")
worksheet3.write(0,2,"Headline 1")
worksheet3.write(0,3,"Headline 2")
worksheet3.write(0,4,"Description")
worksheet3.write(0,5,"Path1")
worksheet3.write(0,6,"Path2")
worksheet3.write(0,7,"Final URL")
    
row = 1
for categoria in all_p:
    for x in categoria:
        
        worksheet3.write(row,0,x.campanha)
        worksheet3.write(row,1,x.nome)
        worksheet3.write(row,2,x.nome)
        worksheet3.write(row,3,'bringIT Especialista Telas') 
        worksheet3.write(row,4,x.desc)
        worksheet3.write(row,5,'bringit')
        worksheet3.write(row,6,'teclado')
        worksheet3.write(row,7,x.link)

        row = row+1        

hj = str(date.today())
workbook.save(r"C:\Users\a000043\Desktop\adwords-" +hj+".xls")

print('Planilha salva!')





    
