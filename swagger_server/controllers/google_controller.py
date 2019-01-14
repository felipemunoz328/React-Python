import connexion
import six

from swagger_server.models.get_lat_lon import GetLatLon  # noqa: E501
from swagger_server import util


def get_latlon_get(body):  # noqa: E501
    """obtener tiempo estimado

     # noqa: E501

    :param body: hello
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = GetLatLon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
