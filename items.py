# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags



class inova_item (scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    modalidade = scrapy.Field(output_processor=TakeFirst())
    leilao = scrapy.Field(output_processor=TakeFirst())
    leiloeiro = scrapy.Field(output_processor=TakeFirst())
    local_leilao = scrapy.Field(output_processor=TakeFirst())
    abertura_primeiro = scrapy.Field(output_processor=TakeFirst())
    fechamento_primeiro = scrapy.Field(output_processor=TakeFirst())
    valor_primeiro = scrapy.Field(output_processor=TakeFirst())
    abertura_segundo = scrapy.Field(output_processor=TakeFirst())
    fechamento_segundo = scrapy.Field(output_processor=TakeFirst())
    valor_segundo = scrapy.Field(output_processor=TakeFirst())
    incremento = scrapy.Field(output_processor=TakeFirst())
    avaliacao = scrapy.Field(output_processor=TakeFirst())
    visitas = scrapy.Field(output_processor=TakeFirst())
    ultimo_lance = scrapy.Field(output_processor=TakeFirst())
    descricao = scrapy.Field(output_processor=TakeFirst())
    imagem = scrapy.Field(output_processor=TakeFirst())
