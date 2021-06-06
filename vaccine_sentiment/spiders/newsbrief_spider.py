import scrapy


class NewsbriefSpider(scrapy.Spider):
    name = 'newsbrief_spider'
    pages = 1000
    start_urls = [f'https://emm.newsbrief.eu/NewsBrief/dynamic?language=en&page={page}&edition=searcharticles&option=advanced&atLeast=Astrazeneca%2C+Pfizer%2C+Moderna%2C+Vaccine%2C+BioNTech%2C+Vaccination%2C+Johnson+%26+Johnson&dateFrom=2021-01-08&dateTo=2021-06-06&lang=en&source=ABCnews&source=foxnews&source=nytimes&_=1622985903001'
                  for page in range(pages)]
    urls = []

    def parse(self, response):
        links = response.xpath("//a[contains(@class,'headline_link')]/@href").extract()
        links_with_nl = [l + "\n" for l in links]
        with open("links.txt", 'a') as f:
            f.writelines(links_with_nl)
            f.close()
