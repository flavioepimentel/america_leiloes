# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class SpiderleilaoPipeline:
    def __init__(self):
        self.conexao = sqlite3.connect('inova.db')
        self.cursor = self.conexao.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inovaDB
            (
            id 	INTEGER,
            title text,
            modalidadbe text,
            leilao text,
            leiloeiro text,
            local_leilao text,
            abertura_primeiro text,
            fechamento_primeiro text,
            valor_primeiro text,
            abertura_segundo text,
            fechamento_segundo text,
            valor_segundo text,  
            incremento text,
            avaliacao text,
            visitas text,
            ultimo_lance text,
            descricao text,
            imagem text     
               )''')



    def process_item(self, item, spider):
        self.cursor.execute("""INSERT OR IGNORE INTO inovaDB""")
        return item
