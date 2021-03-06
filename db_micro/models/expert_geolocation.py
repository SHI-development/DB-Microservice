# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from db_micro.models.base_model_ import Model
from db_micro.models.geolocation import Geolocation
from db_micro import util


class ExpertGeolocation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, lat: float=None, lon: float=None):  # noqa: E501
        """ExpertGeolocation - a model defined in Swagger

        :param lat: The lat of this ExpertGeolocation.  # noqa: E501
        :type lat: float
        :param lon: The lon of this ExpertGeolocation.  # noqa: E501
        :type lon: float
        """
        self.swagger_types = {
            'lat': float,
            'lon': float
        }

        self.attribute_map = {
            'lat': 'lat',
            'lon': 'lon'
        }

        self._lat = lat
        self._lon = lon

    @classmethod
    def from_dict(cls, dikt) -> 'ExpertGeolocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Expert_geolocation of this ExpertGeolocation.  # noqa: E501
        :rtype: ExpertGeolocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lat(self) -> float:
        """Gets the lat of this ExpertGeolocation.


        :return: The lat of this ExpertGeolocation.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat: float):
        """Sets the lat of this ExpertGeolocation.


        :param lat: The lat of this ExpertGeolocation.
        :type lat: float
        """

        self._lat = lat

    @property
    def lon(self) -> float:
        """Gets the lon of this ExpertGeolocation.


        :return: The lon of this ExpertGeolocation.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon: float):
        """Sets the lon of this ExpertGeolocation.


        :param lon: The lon of this ExpertGeolocation.
        :type lon: float
        """

        self._lon = lon
