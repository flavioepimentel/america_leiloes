# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import itemloaders
import scrapy
from ..items import inova_item
from scrapy.loader import ItemLoader


class inovaSpider(scrapy.Spider):
    name = 'inova'
    allowed_domains = ['www.inovaleilao.com.br']
    start_urls = [
        'https://www.inovaleilao.com.br/'
    ]

    # Conexão com página inicial 'https://www.inovaleilao.com.br/'
    def parse(self, response):
        # Filtrando @href do menu dropdown
        page = response.xpath('//nav//div//ul//li//div//div/a[re:test(@href, "categorias/imoveis")]/@href').get() 
        # Fazendo requisição na opção do menu 
        yield scrapy.Request(response.urljoin(page), callback=self.parse_cards)
        
    # Lidando com a requisição
    def parse_cards(self, response):
        # Listando todos os cards disponíveis de oportunidades por seu @href
        cards = response.css("a.btn.btn-link.rounded-lg.btn-block.bg-3.text-white::attr(href)").getall()
        # Fazendo uma requisição para cada @href encontrado
        for card in cards:
            yield scrapy.Request(response.urljoin(card), callback=self.parse_imoveis)

    # Raspando dados das oportunidades
    def parse_imoveis(self, response):


        # Convertendo a resposta em modelo de dicionário
        yield {
            'title': response.css('h2.h5.text-center.text-md-right.text-lg-left.mb-md-0.fc-1::text').get(),
            "abertura_primeiro":response.css('td.text-center.text-sm-left::text')[0].get(),
            "fechamento_primeiro": response.css('td.text-center.text-sm-left::text')[1].get(),
            "valor_primeiro": response.css('td.p-2.align-middle::text')[2].get(),
            "abertura_segundo": response.css('td.text-center.text-sm-left::text')[2].get(),
            "fechamento_segundo": response.css('td.text-center.text-sm-left::text')[3].get(),
            "valor_segundo": response.css('td.p-2.align-middle::text')[5].get(),  
            "incremento": response.css('dd.d-inline-block.mb-0::text')[0].get(),
            "avaliacao": response.css('dd.d-inline-block.mb-0::text')[1].get(),
            "visitas": response.css('dd.d-inline-block.mb-0::text')[2].get(),
            "ultimo_lance": response.xpath('//div/div/div/div/table/tbody/tr/td[re:test(@class, "text-center align-middle")]//text()')[0:4].getall(),
            "descricao": response.css('p::text')[2:-3].getall(),
            "imagem": response.css('img.w-100::attr(src)').get(),         
        }
