#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from datetime import datetime

from elasticsearch import helpers
from elasticsearch import Elasticsearch
from elasticsearch import ConnectionError
from elasticsearch import NotFoundError
from elasticsearch import RequestError

es = Elasticsearch()


class ElasticsearchCreator(object):

    @staticmethod
    def bulk_load(actions_):
        """Performs the bulk load to Elasticsearch
        """
        for i in actions_:
            i['_source']['created_at'] = datetime.now()
        res = None
        try:
            res = helpers.parallel_bulk(es, actions_)
        except Exception as e:
            print("There was an error")
            print(e)
        return res

    @staticmethod
    def process_result(result_list):
        success, fail = 0, 0
        for i in result_list:
            if i[0]:
                success = success + 1
            else:
                fail = fail + 1
        return success, fail
