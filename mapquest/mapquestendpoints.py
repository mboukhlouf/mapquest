from .endpointdata import EndpointData

api_url = "http://www.mapquestapi.com"


def get_url(endpoint):
    return api_url + endpoint


endpoints = {
    "directions": {
        "route": EndpointData(get_url("/directions/v2/route"), True),
        "optimizedroute": EndpointData(get_url("/directions/v2/optimizedroute"), True),
        "routematrix": EndpointData(get_url("/directions/v2/routematrix"), True),
        "alternateroutes": EndpointData(get_url("/directions/v2/alternateroutes"), True),
        "pathfromroute": EndpointData(get_url("/directions/v2/pathfromroute"), True),
        "findlinkid": EndpointData(get_url("/directions/v2/findlinkid"), True),
    },
    "geocoding": {
        "address": EndpointData(get_url("/geocoding/v1/address"), True),
        "reverse": EndpointData(get_url("/geocoding/v1/reverse"), True),
        "batch": EndpointData(get_url("/geocoding/v1/batch"), True),
    }
}
