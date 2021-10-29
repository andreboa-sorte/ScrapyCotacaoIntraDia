import scrapy


class CotacaoSpider(scrapy.Spider):
    name = 'cotacao'
    #allowed_domains = ['valorinveste.globo.com/cotacoes']
    start_urls = ['http://valorinveste.globo.com/cotacoes/'] # o link q sera "scrapydo".
                                                                        # como é somente vamos pegar os dados de um dominio,
                                                                        # então não vamos usar o allowed_domains

    def parse(self, response):
        dataDosDados = response.xpath('//*[@id="cotacoes-intradia"]/div/div[2]/div/div[1]/h2/text()').extract_first()
        lista = response.xpath('//*[@id="cotacoes-intradia"]/div/div[2]/div/div[2]/table/tbody/tr')
        i = 0
        for itemlita in lista:  # um laço de repetição para pegar todos os dados da "caixa grande"
            i = int(i) #como é um laço de repetição, o i que abaixo se trasnformou em STR, tem q voltar a ser int, para poder ser incrementado
            i = i + 1
            i = str(i) #transforma o i em str para poder ser adicionado a string do Xpath
            # aqui nesse parte onde é pego os dados que se deseja exrair e é botado nas variaveis
            nome  = itemlita.xpath('//*[@id="cotacoes-intradia"]/div/div[2]/div/div[2]/table/tbody/tr['+i+']/td[1]/text()').extract_first()
            codigo  = itemlita.xpath('//*[@id="cotacoes-intradia"]/div/div[2]/div/div[2]/table/tbody/tr['+i+']/td[2]/text()').extract_first()
            ultimaCotacao  = itemlita.xpath('//*[@id="cotacoes-intradia"]/div/div[2]/div/div[2]/table/tbody/tr['+i+']/td[3]/text()').extract_first()
            variacao  = itemlita.xpath('//*[@id="cotacoes-intradia"]/div/div[2]/div/div[2]/table/tbody/tr['+i+']/td[4]/text()').extract_first()
            fechDiaAnt = itemlita.xpath('//*[@id="cotacoes-intradia"]/div/div[2]/div/div[2]/table/tbody/tr['+i+']/td[5]/text()').extract_first()

            yield {  # depois de coletados, as informações são organizadas para q possão ser salvas e são salvas depois
                'dataDosDados': dataDosDados,
                'nome': nome,
                'codigo': codigo,
                'ultimaCotacao': ultimaCotacao,
                'variacao': variacao,
                'fechDiaAnt': fechDiaAnt,
            }