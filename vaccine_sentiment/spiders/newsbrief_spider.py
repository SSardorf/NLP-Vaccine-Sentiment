import scrapy


class NewsbriefSpider(scrapy.Spider):
    name = 'newsbrief_spider'
    pages = 1000
    start_urls = [f'https://emm.newsbrief.eu/NewsBrief/dynamic?language=en&page={start_page}&edition=searcharticles' \
                  f'&option=advanced&atLeast=vaccine&dateFrom=2021-01-12&dateTo=2021-05-31&lang=en&source=ABCnews' \
                  f'&source=cnn&source=foxnews&source=nytimes&source=huffingtonpost-us-en&sourceCountry=US&_' \
                  f'=1622811590941 '
                  for start_page in range(pages)]
    urls = []

    def parse(self, response):
        links = response.xpath("//a[contains(@class,'headline_link')]/@href").extract()
        links_with_nl = [l + "\n" for l in links]
        with open("links.txt", 'a') as f:
            f.writelines(links_with_nl)
            f.close()

# https://emm.newsbrief.eu/NewsBrief/searchresults/en/advanced.html?lang=en&sourceCountry=US&source=ABCnews%2Ccnn%2Cfoxnews%2Cnytimes%2Chuffingtonpost-us-en&atLeast=vaccine&dateFrom=2021-01-12&dateTo=2021-05-31&queryType=advanced

