import connexion
import six
import requests
import json
import urllib
from uber_request import get_time_estimate

from urllib.parse import quote, urlencode
from pprint import pprint
from uber_rides.session import Session
from uber_rides.client import UberRidesClient


from swagger_server.models.estimated_time import EstimatedTime  # noqa: E501
from swagger_server import util


def get_time_post(body):  # noqa: E501
    """obtener tiempo estimado con las locaciones

     # noqa: E501

    :param body: hello
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = EstimatedTime.from_dict(connexion.request.get_json())  # noqa: E501
        print(type(body.longitud_final))
        estimate = get_time_estimate(body.longitud_inicial,body.latitud_inicial,body.longitud_final,body.latitud_final)

    return estimate
