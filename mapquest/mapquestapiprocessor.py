import json
import urllib.parse
import urllib.request


class MapQuestApiProcessor:
    def __init__(self, key):
        self.key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    def request(self, endpoint, **data):
        if endpoint.authentication:
            data["key"] = self.key
        query_string = urllib.parse.urlencode(data)
        url = endpoint.url + "?" + query_string
        f = urllib.request.urlopen(url)
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data
