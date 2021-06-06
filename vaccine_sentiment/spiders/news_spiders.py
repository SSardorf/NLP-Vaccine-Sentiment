import scrapy
import pandas as pd
import datetime

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
            "Accessed": datetime.datetime.today(),
            "Title":response.css("h1::text").get(),
            "Channel": "Fox News",
            "Date": response.css("time::text").get(),
            "URL": response.request.url,
            "Content": " ".join(response.xpath("//div[contains(@class, 'article-body')]/p/text()|//div[contains(@class, 'article-body')]/p/a/text()|//div[contains(@class, 'article-body')]/p/em/text()").getall()),
        }

class AbcSpider(scrapy.Spider):
    name = 'abc_spider'
    allowed_domains = ['abcnews.go.com']
    start_urls = []
    df = pd.DataFrame(columns=['URL', 'Title', 'Date', 'Content', 'Channel'])
    with open("links.txt", "r") as f:
        for i in f.read().splitlines():
            if i.startswith("https://abcnews.go.com"):
                start_urls.append(i)

    def parse(self, response, df=df):
        yield {
            "Accessed": datetime.datetime.today(),
            "Title":response.css("h1::text").get(),
            "Channel": "ABC News",
            "Date": response.xpath("//div[contains(@class, 'Byline__Meta--publishDate')]/text()").get(),
            "URL": response.request.url,
            "Content": " ".join(response.xpath("//section[contains(@class, 'story')]/p/text()|//section[contains(@class, 'story')]/p/a/text()|//section[contains(@class, 'story')]/p/em/text()").getall()),
        }

class CbsSpider(scrapy.Spider):
    name = 'cbs_spider'
    allowed_domains = ['cbslocal.com']
    start_urls = []
    df = pd.DataFrame(columns=['URL', 'Title', 'Date', 'Content', 'Channel'])
    with open("links.txt", "r") as f:
        for i in f.read().splitlines():
            if 'cbslocal.com' in i:
                start_urls.append(i)

    def parse(self, response, df=df):
        yield {
            "Accessed": datetime.datetime.today(),
            "Title":response.css("h1::text").get(),
            "Channel": "CBS News",
            "Date": response.xpath("//time[contains(@class, 'post-date')]/text()").get(),
            "URL": response.request.url,
            "Content": " ".join(response.xpath("//div[contains(@class, 'main-story-wrapper')]/p/text()").getall()),
        }

class CnnSpider(scrapy.Spider):
    name = 'cnn_spider'
    allowed_domains = ['cnn.com']
    start_urls = []
    df = pd.DataFrame(columns=['URL', 'Title', 'Date', 'Content', 'Channel'])
    with open("links.txt", "r") as f:
        for i in f.read().splitlines():
            if i.startswith("https://edition.cnn.com"):
                start_urls.append(i)

    def parse(self, response, df=df):
        yield {
            "Accessed": datetime.datetime.today(),
            "Title":response.css("h1::text").get(),
            "Channel": "CNN News",
            "Date": response.xpath("//div[contains(@class, 'Article__subtitle')]/text()")[-1].get(),
            "URL": response.request.url,
            "Content": " ".join(response.xpath("//div[contains(@class, 'Article__body')]//span/text()").getall()),
        }

class NytSpider(scrapy.Spider):
    name = 'nyt_spider'
    allowed_domains = ['nytimes.com']
    start_urls = []
    df = pd.DataFrame(columns=['URL', 'Title', 'Date', 'Content', 'Channel'])
    with open("links.txt", "r") as f:
        for i in f.read().splitlines():
            if i.startswith("https://www.nytimes.com"):
                start_urls.append(i)

    def parse(self, response, df=df):
        date_response = response.xpath("//time/text()|//time/span/text()").getall()
        if "published" not in date_response[0].lower():
            date = date_response[0]
        else:
            date = date_response[1]
        yield {
            "Accessed": datetime.datetime.today(),
            "Title":response.css("h1::text").get(),
            "Channel": "New York Times",
            "Date": date,
            "URL": response.request.url,
            "Content": " ".join(response.xpath("//section[contains(@name, 'articleBody')]//p/text()|//section[contains(@name, 'articleBody')]//p/a/text()|//section[contains(@name, 'articleBody')]//p/em/text()").getall()),
        }

class HufSpider(scrapy.Spider):
    name = 'huf_spider'
    allowed_domains = ['www.huffpost.com']
    custom_settings = {
        'COMPRESSION_ENABLED':False
    }
    start_urls = []
    df = pd.DataFrame(columns=['URL', 'Title', 'Date', 'Content', 'Channel'])
    with open("links.txt", "r") as f:
        for i in f.read().splitlines():
            if i.startswith("https://www.huffpost.com"):
                start_urls.append(i)

    def parse(self, response, df=df):
        yield {
            "Accessed": datetime.datetime.today(),
            "Title":response.css("h1::text").get(),
            "Channel": "Huffpost",
            "Date": response.xpath("//span[contains(@class, 'timestamp__date--published')]/span/text()").get(),
            "URL": response.request.url,
            "Content": " ".join(response.xpath("//div[contains(@class, 'entry__text')]//p/text()").getall()),
        }
