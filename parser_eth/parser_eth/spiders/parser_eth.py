import scrapy


class ETHSpider(scrapy.Spider):
    name = 'eth'
    allowed_domains = ['www.binance.com']
    start_urls = [
        'https://www.binance.com/ru/trade/ETH_USDT?theme=dark&type=spot'
    ]

    def parse(self, response,):
        crypto_price = response.css('div.layout')
        yield crypto_price
