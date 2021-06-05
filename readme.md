## Installation

*  Run `pip install -r requirements.txt`

## Run the spiders
#### Individually
To run an individual spider and save the results to a csv file you can do the following

`scrapy crawl {name of spider} -O filename.csv`

So if we want to scrape the fox links, we can simply run this

`scrapy crawl fox_spider -O fox.csv`

#### Aggregate run
To run all the spiders and aggregate the result to a single csv file, I've made this command you can run

``` scrapy crawl huf_spider -o aggregate.csv && scrapy crawl nyt_spider -o aggregate.csv && scrapy crawl cnn_spider -o aggregate.csv && scrapy crawl cbs_spider -o aggregate.csv && scrapy crawl abc_spider -o aggregate.csv && scrapy crawl fox_spider -o aggregate.csv```

This will save an aggregate result to a csv file