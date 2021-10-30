# ScrapyCotacaoIntraDia

![Sem título](https://user-images.githubusercontent.com/53584953/139541950-6ba814d5-c168-4ca2-bd79-0ef92595423c.png)

## Objetivo: coletar os dados de cotação intra dia do site https://valorinveste.globo.com 


### Demostração de como a informação é aprensetada no site:
![salvar exemplo de como é apresentado os dados](https://user-images.githubusercontent.com/53584953/139541959-7a9330b2-01fb-4422-8ace-235d7591916d.png)

***

## Informações sobre o codigo

<strong>Itens ultilizados e versoniamentos:</strong>
* Python 3.9.0
* Scrapy 2.4.1 

<strong>Preciso baixar algo?</strong><br>
É necessario ter o Python instalado e o Scrapy (*pip install scrapy*); Por ultimo, ter uma IDE de sua preferencia, para rodar o projeto.<br>

<strong>Como faço para funcionar o codigo?</strong>
* Basta baixar ou clonar o codigo, caso não tenha instalado o <strong>Scrapy</strong>, instale ele (*pip install scrapy*).
* Abra o terminal e esteja dentro da pasta do projeto, depois basta rodar o comando: <br>
 **scrapy crawl cotacao -o** *(nome do arquivo a ser gerado + .csv ou qualquer extensão desejada)*.<br>
 **Exemplo**: scrapy crawl cotacao -o DadosCotacaoIntraDia.csv
 
 ![teminal](https://user-images.githubusercontent.com/53584953/139542273-d5b9aac3-b246-4db7-9a37-afaf2c51491e.png)

 ### Onde vejo o codigo que foi criado e posso alteralo?
#### Caso deseja alterar a esturua do codigou ou A estrutura do site seja alterada e o Xpaht não funione mais.

* Entre na pasta *Spiders*, abra o arquivo **cotacao** e lá será encontrado todos o codigo feito e seu comentario explicando cada função.

![pastas](https://user-images.githubusercontent.com/53584953/139542282-1b8fee2a-f1fd-40d5-9b61-97c396531979.png)

