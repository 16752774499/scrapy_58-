import scrapy
from wuba.items import WubaItem
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options  # 无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
from selenium.webdriver import ChromeOptions  # 规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
bot = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options, options=option)

class Wuba1Spider(scrapy.Spider):
    name = 'wuba_1'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'https://xianyang.58.com/job/?param7503=1&from=yjz2_zhaopin&utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d202408-01d1-d86d-1573-f4faec6defb1&ClickID=4']
    #设置通用url模板
    url = 'https://xianyang.58.com/job/pn%d/?param7503=1&from=yjz2_zhaopin&utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d302408-01d1-d5f6-40be-8cb0310f3453&ClickID=3'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//ul[@id="list_con"]/li')
        for li in li_list:
            #实例化一个item
            item = WubaItem()
            # 解析工作岗位
            name = li.xpath('./div/div/a/span[2]/text()')[0].extract()
            #解析详情页url
            deta_url = li.xpath('./div/div/a/@href')[0].extract()
            deta_url = ''.join(deta_url)
            new_url = str(deta_url)
            item['new_url'] = new_url
            bot.get(new_url)
            page = bot.page_source
            tree = etree.HTML(page)
            #解析工资
            gongci = tree.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/span[2]//text()')
            gongci = ''.join(gongci)
            #解析学历
            yueli = tree.xpath('/html/body/div[3]/div[3]/div[1]/div[4]/span[2]//text()')[0]
            #                   /html/body/div[3]/div[3]/div[1]/div[4]/span[2]
            #提交item
            item['gongci'] = gongci
            item['yueli'] = yueli
            item['name'] = name
            yield item
        #进行分页操作
        if self.page_num <= 5:
            num_url = format(self.url%self.page_num)
            self.page_num+=1
            yield scrapy.Request(url=num_url,callback=self.parse)

