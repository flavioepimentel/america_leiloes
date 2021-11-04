import scrapy

class inovaSpider(scrapy.Spider):
    name = 'inova'
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
        title = response.css('h2.h5.text-center.text-md-right.text-lg-left.mb-md-0.fc-1::text').get()
        modalidade = response.css('td.border-0::text')[0].get()


        #@Dev - Ponto de melhoria: lógica do local do leilão, necessário validação com if
        #local_leilao = response.css('td.border-0::text')[1].get()
        
        leilao = response.css('td.border-0::text')[1].get()
        leiloeiro = response.css('td.border-0::text')[2].get()
        id = response.css('td.border-0::text')[3].get()
        abertura_primeiro = response.css('td.text-center.text-sm-left::text')[0].get()
        fechamento_primeiro = response.css('td.text-center.text-sm-left::text')[1].get()
        valor_primeiro = response.css('td.p-2.align-middle::text')[2].get()
        abertura_segundo = response.css('td.text-center.text-sm-left::text')[2].get()
        fechamento_segundo = response.css('td.text-center.text-sm-left::text')[3].get()
        valor_segundo = response.css('td.p-2.align-middle::text')[5].get()
        incremento = response.css('dd.d-inline-block.mb-0::text')[0].get()
        avaliacao = response.css('dd.d-inline-block.mb-0::text')[1].get()
        visitas = response.css('dd.d-inline-block.mb-0::text')[2].get()

        # Coletando o último lance em formato de lista - Valor Indicie:[1]; Data Indicie:[2]
        ultimo_lance = response.xpath('//div/div/div/div/table/tbody/tr/td[re:test(@class, "text-center align-middle")]//text()')[0:4].getall()


        yield {
            'id': id,
            'title': title,
            'modalidae': modalidade,
            'leilao': leilao,
            'leiloeiro': leiloeiro,
            "abertura_primeiro": abertura_primeiro,
            "fechamento_primeiro": fechamento_primeiro,
            "valor_primeiro": valor_primeiro,
            "abertura_segundo": abertura_segundo,
            "fechamento_segundo": fechamento_segundo,
            "valor_segundo": valor_segundo,           
        }
