# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mijob2.items import Mijob2Item
from scrapy.selector import Selector
import re


class MijobspiderSpider(CrawlSpider):
    name = 'mijobspider'
    allowed_domains = ['hr.xiaomi.com']
    start_urls = ['http://hr.xiaomi.com/job/list/0-0-2-0-1']

    rules = (
        Rule(LinkExtractor(allow='http://hr.xiaomi.com/job/view/', restrict_xpaths='//tbody/tr/td/a'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='hr.xiaomi.com/job/list', restrict_xpaths='//a[@class="numbers last"]'),
             follow=True),
    )

    def parse_item(self, response):
        se = Selector(response)
        item = Mijob2Item()
        jobname = se.xpath('//tr[1]/td[2]/text()')
        jobaddress = se.xpath('//tr[1]/td[4]/text()')
        jobclass = se.xpath('///tr[2]/td[2]/text()')
        jobchannel = se.xpath('//tr[2]/td[4]/text()')
        jobduty = se.xpath('//tr[3]/td[2]')
        jobrequ = se.xpath('//tr[4]/td[2]')
        item['jobname'] = jobname.extract()
        item['jobaddress'] = jobaddress.extract()
        item['jobclass'] = jobclass.extract()
        item['jobchannel'] = jobchannel.extract()
        item['jobduty'] = jobduty.extract()
        item['jobrequ'] = jobrequ.extract()
        yield item
