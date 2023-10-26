class ElasURLs:
    def __init__(self, name):
        self.name = name

    def elas_url(self):
        url_dict = {
            "cmhl": "https://cmhl-es.kernellix.net:443",
            "mit": "https://mit-es.kernellix.net:443",
            "zait": "https://zait-es.kernellix.net:443",
            "ccn": "https://ccn-es.kernellix.net:443",
            "oway": "https://oway-es.kernellix.net:443",
            "auderbox": "https://adb-es.kernellix.net:443",
            "dev": "https://dev-es.kernellix.net:443"
        }

        return url_dict[self.name]
