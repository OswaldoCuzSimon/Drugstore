
from elasticsearch import helpers
from elasticsearch import Elasticsearch
from elasticsearch import ConnectionError
from elasticsearch import NotFoundError
from elasticsearch import RequestError

es = Elasticsearch()


class ElasticsearchReader(object):

    @staticmethod
    def get_last_id(index, doctype):
        """Get the last ID for autoincremental ID generation"""
        _query = {
            "size": 1,
            "sort": {"created_at": "desc"},
            "query": {
                "match_all": {}
            }
        }
        _filter_path = 'hits.hits._id'
        try:
            result = es.search(
                index=index,
                doc_type=doctype,
                body=_query,
                filter_path=_filter_path)
        except ConnectionError as error:
            raise error

        try:
            return int(result['hits']['hits'][0]['_id'])
        except (TypeError, KeyError):
            return 0
