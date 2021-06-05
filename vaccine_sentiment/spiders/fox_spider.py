import scrapy
import pandas as pd

class FoxSpider(scrapy.Spider):
    name = 'fox_spider'
    allowed_domains = ['foxnews.com']
    start_urls = []
    df = pd.DataFrame(columns=['URL', 'Title', 'Date', 'Content', 'Channel'])
    with open("links.txt", "r") as f:
        for i in f.read().splitlines():
            if i.startswith("https://www.foxnews.com"):
                start_urls.append(i)

    def parse(self, response, df=df):
        yield {
            "Title":response.css("h1::text").get(),
            "Channel": "Fox News",
            "Date": response.css("time::text").get(),
            "URL": response.request.url,
            "Content": " ".join(response.xpath("//div[contains(@class, 'article-body')]/p/text()").getall()),
        }
# https://emm.newsbrief.eu/NewsBrief/searchresults/en/advanced.html?lang=en&sourceCountry=US&source=ABCnews%2Ccnn%2Cfoxnews%2Cnytimes%2Chuffingtonpost-us-en&atLeast=vaccine&dateFrom=2021-01-12&dateTo=2021-05-31&queryType=advanced

