import scrapy
from ganme_news.items import GanmeNewsItem
class mySpider(scrapy.Spider):
    name = 'game_news'

    start_urls = ['https://www.3dmgame.com/news_all_{}/'.format(page) for page in range(5000)]

    def parse(self, response):
        ul = response.xpath("//ul[@class='list']")
        urls = ul.xpath("li/a/@href").extract()
        bts = ul.xpath("li/a/div[@class='bt']/text()").extract()
        times = ul.xpath("li/a/div/span[@class='time']/text()").extract()
        news_list = list(zip(bts,urls,times))
        for news in news_list:
            game = GanmeNewsItem()
            game['bt'] = news[0]
            game['url'] = news[1]
            game['time'] = news[2]

            yield game

