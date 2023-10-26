from ElasApikeys import ElasAPIkeys
from ElasURLs import ElasURLs
from elasticsearch import Elasticsearch


class ElasConnect:

    def __init__(self, name):
        self.name = name

    def elas_connect(self):
        elasticsearch_url = ElasURLs(f"{self.name}").elas_url()
        apikey = ElasAPIkeys(f"{self.name}").elas_apikey()

        es = Elasticsearch(
            elasticsearch_url,
            api_key=(apikey["apikey_id"], apikey["apikey_secret"])
        )

        return es
