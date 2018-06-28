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
            res = list(res)
            es.indices.refresh(index="inventory")
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

    @staticmethod
    def get_actions_id_auto_increment(index, doctype, data_list):
        new_id = ElasticsearchCreator.get_last_id(index, doctype)
        for i in range(len(data_list)):
            new_id += 1
            data_list[i] = {
                "_index": index,
                "_id": new_id,
                "_type": doctype,
                "_source": data_list[i]
            }
        return data_list

    @staticmethod
    def get_actions(index, doctype, data_list):
        return [{
            "_index": index,
            "_type": doctype,
            "_source": i
        } for i in data_list]
