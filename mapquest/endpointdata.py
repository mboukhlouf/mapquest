class EndpointData:
    def __init__(self, url, authentication):
        self.url = url
        self.authentication = authentication

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def authentication(self):
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        self._authentication = authentication
