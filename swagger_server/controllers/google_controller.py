import connexion
import six

from swagger_server.models.get_lat_lon import GetLatLon  # noqa: E501
from swagger_server import util
from google_request import get_coordinades


def get_latlon_get(body):  # noqa: E501
    """obtener tiempo estimado

     # noqa: E501

    :param body: hello
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # noqa: E501

        #print(body["Destino"])
        #inicio 
        direccionI = body["inicio"]["address"]
        numeroI = str(body["inicio"]["number"])
        comunaI = body["inicio"]["county"]
        ciudadI = body["inicio"]["city"]
        paisI = body["inicio"]["country"]
        coordenadaI = get_coordinades(direccionI, numeroI, comunaI, ciudadI, paisI)
        #destino
        direccionD = body["destino"]["address"]
        numeroD = str(body["destino"]["number"])
        comunaD = body["destino"]["county"]
        ciudadD = body["destino"]["city"]
        paisD= body["destino"]["country"]
        coordenadaD = get_coordinades(direccionD, numeroD, comunaD, ciudadD, paisD)

        data = {
            "latitud_final": coordenadaD['lat'],
            "latitud_inicial": coordenadaI['lat'],
            "longitud_final": coordenadaD['lng'],
            "longitud_inicial": coordenadaI['lng']
            }
        
    return data
