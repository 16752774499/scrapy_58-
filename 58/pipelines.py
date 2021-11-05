# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WubaPipeline:
    fp = None
    #重写父类方法开启管道
    def open_spider(self,spider):
        print('程序开始')
        self.fp = open('岗位.txt','w',encoding="utf-8")
    #基于管道进行持久化存储
    def process_item(self, item, spider):
        name = item['name']
        gongci = item['gongci']
        yueli = item['yueli']
        new_url = item['new_url']
        self.fp.write(name+':'+gongci+'\n'+yueli+':详情页url:'+'"'+new_url+'"'+  '\n')
        return item
    #重写父类方法关闭管道
    def close_spider(self,spider):
        print('程序结束')
        self.fp.close()
