import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    # retiramos o allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for movies in response.css('.titleColumn'):
            yield{
                'titles': movies.css('.titleColumn a::text').get(),
                'years': movies.css('.secondaryInfo::text').get(),
                'evaluation': response.css('strong::text').get(),               
            }
            
            # coloquei 'movies' em titles e years porque estes estão dentro da mesma caixa de 'movies'
