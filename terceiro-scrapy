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
        lista = response.css('td.border-0::text').getall()

        # Difinindo il como o carregamento de itens 
        il = ItemLoader(item=inova_item(), selector=response)
        il.add_css('title', 'h2.h5::text')
        # Verificando se na tabela constam todos os dados
        if len(lista) > 4:
            il.add_css('modalidade', 'td.border-0::text')
            il.add_css('local_leilao', 'td.border-0::text')
            il.add_css('leilao', 'td.border-0::text')
            il.add_css('leiloeiro', 'td.border-0::text')
            il.add_css('id', 'td.border-0::text')
            
        else:
            il.add_css('modalidade', 'td.border-0::text')
            il.add_css('leilao', 'td.border-0::text')
            il.add_css('leiloeiro', 'td.border-0::text')
            il.add_css('id', 'td.border-0::text')
        
        il.add_css('abertura_primeiro', 'td.text-center::text')
        il.add_css('fechamento_primeiro', 'td.text-center::text')
        il.add_css('valor_primeiro', 'td.p-2::text')
        il.add_css('abertura_segundo', 'td.text-center::text')
        il.add_css('fechamento_segundo', 'td.text-center::text')
        il.add_css('valor_segundo', 'td.p-2::text')
        il.add_css('incremento', 'dd.d-inline-block::text')
        il.add_css('avaliacao', 'dd.d-inline-block::text')
        il.add_css('visitas', 'dd.d-inline-block::text')
        il.add_xpath('ultimo_lance', '//td[re:test(@class, "text-center align-middle")]//text()')
        il.add_css('descricao', 'p::text')
        il.add_css('imagem', 'img.w-100::attr(src)')

        yield il.load_item()
