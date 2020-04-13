from .mapquestendpoints import endpoints
from .mapquestapiprocessor import MapQuestApiProcessor


class MapQuestClient:
    def __init__(self, key):
        self._key = key
        self._api_processor = MapQuestApiProcessor(key)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
        self._api_processor.key = key

    def address(self, **params):
        return self._api_processor.request(endpoints["geocoding"]["address"], **params)

    def reverse(self, **params):
        return self._api_processor.request(endpoints["geocoding"]["reverse"], **params)

    def batch(self, **params):
        return self._api_processor.request(endpoints["geocoding"]["batch"], **params)

    def route(self, **params):
        return self._api_processor.request(endpoints["directions"]["route"], **params)

    def optimized_route(self, **params):
        return self._api_processor.request(endpoints["directions"]["optimizedroute"], **params)

    def route_matrix(self, **params):
        return self._api_processor.request(endpoints["directions"]["routematrix"], **params)

    def alternate_routes(self, **params):
        return self._api_processor.request(endpoints["directions"]["alternateroutes"], **params)

    def path_from_route(self, **params):
        return self._api_processor.request(endpoints["directions"]["pathfromroute"], **params)

    def find_link_id(self, **params):
        return self._api_processor.request(endpoints["directions"]["findlinkid"], **params)