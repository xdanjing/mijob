# -*- coding: utf-8 -*-

import scrapy


class Mijob2Item(scrapy.Item):
    # define the fields for your item here like:
    jobname = scrapy.Field()
    jobaddress = scrapy.Field()
    jobclass = scrapy.Field()
    jobchannel = scrapy.Field()
    jobduty = scrapy.Field()
    jobrequ = scrapy.Field()

