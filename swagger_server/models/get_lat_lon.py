# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetLatLon(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, address: str=None, number: int=None, comuna: str=None, ciudad: str=None, pais: str=None):  # noqa: E501
        """GetLatLon - a model defined in Swagger

        :param address: The address of this GetLatLon.  # noqa: E501
        :type address: str
        :param number: The number of this GetLatLon.  # noqa: E501
        :type number: int
        :param comuna: The comuna of this GetLatLon.  # noqa: E501
        :type comuna: str
        :param ciudad: The ciudad of this GetLatLon.  # noqa: E501
        :type ciudad: str
        :param pais: The pais of this GetLatLon.  # noqa: E501
        :type pais: str
        """
        self.swagger_types = {
            'address': str,
            'number': int,
            'comuna': str,
            'ciudad': str,
            'pais': str
        }

        self.attribute_map = {
            'address': 'address',
            'number': 'number',
            'comuna': 'comuna',
            'ciudad': 'ciudad',
            'pais': 'pais'
        }

        self._address = address
        self._number = number
        self._comuna = comuna
        self._ciudad = ciudad
        self._pais = pais

    @classmethod
    def from_dict(cls, dikt) -> 'GetLatLon':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get_lat_lon of this GetLatLon.  # noqa: E501
        :rtype: GetLatLon
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self) -> str:
        """Gets the address of this GetLatLon.


        :return: The address of this GetLatLon.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this GetLatLon.


        :param address: The address of this GetLatLon.
        :type address: str
        """

        self._address = address

    @property
    def number(self) -> int:
        """Gets the number of this GetLatLon.


        :return: The number of this GetLatLon.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number: int):
        """Sets the number of this GetLatLon.


        :param number: The number of this GetLatLon.
        :type number: int
        """

        self._number = number

    @property
    def comuna(self) -> str:
        """Gets the comuna of this GetLatLon.


        :return: The comuna of this GetLatLon.
        :rtype: str
        """
        return self._comuna

    @comuna.setter
    def comuna(self, comuna: str):
        """Sets the comuna of this GetLatLon.


        :param comuna: The comuna of this GetLatLon.
        :type comuna: str
        """

        self._comuna = comuna

    @property
    def ciudad(self) -> str:
        """Gets the ciudad of this GetLatLon.


        :return: The ciudad of this GetLatLon.
        :rtype: str
        """
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad: str):
        """Sets the ciudad of this GetLatLon.


        :param ciudad: The ciudad of this GetLatLon.
        :type ciudad: str
        """

        self._ciudad = ciudad

    @property
    def pais(self) -> str:
        """Gets the pais of this GetLatLon.


        :return: The pais of this GetLatLon.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais: str):
        """Sets the pais of this GetLatLon.


        :param pais: The pais of this GetLatLon.
        :type pais: str
        """

        self._pais = pais
