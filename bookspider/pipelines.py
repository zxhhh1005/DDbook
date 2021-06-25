# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymysql

class BookspiderPipeline(object):

    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1576596zxh.',db='ddbook',charset='utf8')
        cursor = conn.cursor()
        b_name = item["b_name"][0]
        w_name = item["w_name"][0]
        w_name = w_name.replace(' 著','')
        w_name = w_name.replace('著','')
        w_name = w_name.replace(' 编著','')
        w_name = w_name.replace(' 主编','')
        w_name = w_name.replace(' 编','')
        w_name = w_name.replace('主编：','')
        w_name = w_name.replace('；',' ')
        w_name = w_name.replace('，',' ')
        b_info = item["b_info"]
        b_pic = item["b_pic"]
        p_name = item["p_name"][0]
        s_price = item["s_price"][0].strip('¥')
        pre_price = item["pre_price"][0].strip('¥')
        disc = item["disc"][0].replace('\xa0(','')
        disc = disc.replace('折','')
        disc = disc.replace(') ','')
        p_time = item["p_time"][0].replace(' /','')
        ISBN = item["ISBN"][0].replace('国际标准书号ISBN：','')

        cursor.execute(
            'insert into ddp(b_name,w_name,b_info,b_pic,p_name,s_price,pre_price,disc,p_time,ISBN) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (b_name,w_name,b_info,b_pic,p_name,s_price,pre_price,disc,p_time,ISBN)
        )

        conn.commit()
        cursor.close()

        conn.close()

        return item
