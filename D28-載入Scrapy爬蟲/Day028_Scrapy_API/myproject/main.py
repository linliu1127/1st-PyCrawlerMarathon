import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pathlib import Path


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTcrawler', start_urls=target_urls, filename='test.json')
    process.start()


print(str(Path('.').resolve())+'\myproject\myproject\spiders')
if __name__ == '__main__':  # http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html
    main()
