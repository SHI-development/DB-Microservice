# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from db_micro.models.base_model_ import Model
from db_micro.models.geolocation import Geolocation
from db_micro import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, vatta: float=None, pitta: float=None, kapha: float=None, pub_key: str=None, tasks_completed: List[str]=None, geo_locations: List[Geolocation]=None, orders: List[str]=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: str
        :param vatta: The vatta of this User.  # noqa: E501
        :type vatta: float
        :param pitta: The pitta of this User.  # noqa: E501
        :type pitta: float
        :param kapha: The kapha of this User.  # noqa: E501
        :type kapha: float
        :param pub_key: The pub_key of this User.  # noqa: E501
        :type pub_key: str
        :param tasks_completed: The tasks_completed of this User.  # noqa: E501
        :type tasks_completed: List[str]
        :param geo_locations: The geo_locations of this User.  # noqa: E501
        :type geo_locations: List[Geolocation]
        :param orders: The orders of this User.  # noqa: E501
        :type orders: List[str]
        """
        self.swagger_types = {
            'id': str,
            'vatta': float,
            'pitta': float,
            'kapha': float,
            'pub_key': str,
            'tasks_completed': List[str],
            'geo_locations': List[Geolocation],
            'orders': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'vatta': 'vatta',
            'pitta': 'pitta',
            'kapha': 'kapha',
            'pub_key': 'pub_key',
            'tasks_completed': 'tasksCompleted',
            'geo_locations': 'geoLocations',
            'orders': 'orders'
        }

        self._id = id
        self._vatta = vatta
        self._pitta = pitta
        self._kapha = kapha
        self._pub_key = pub_key
        self._tasks_completed = tasks_completed
        self._geo_locations = geo_locations
        self._orders = orders

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: str
        """

        self._id = id

    @property
    def vatta(self) -> float:
        """Gets the vatta of this User.


        :return: The vatta of this User.
        :rtype: float
        """
        return self._vatta

    @vatta.setter
    def vatta(self, vatta: float):
        """Sets the vatta of this User.


        :param vatta: The vatta of this User.
        :type vatta: float
        """

        self._vatta = vatta

    @property
    def pitta(self) -> float:
        """Gets the pitta of this User.


        :return: The pitta of this User.
        :rtype: float
        """
        return self._pitta

    @pitta.setter
    def pitta(self, pitta: float):
        """Sets the pitta of this User.


        :param pitta: The pitta of this User.
        :type pitta: float
        """

        self._pitta = pitta

    @property
    def kapha(self) -> float:
        """Gets the kapha of this User.


        :return: The kapha of this User.
        :rtype: float
        """
        return self._kapha

    @kapha.setter
    def kapha(self, kapha: float):
        """Sets the kapha of this User.


        :param kapha: The kapha of this User.
        :type kapha: float
        """

        self._kapha = kapha

    @property
    def pub_key(self) -> str:
        """Gets the pub_key of this User.


        :return: The pub_key of this User.
        :rtype: str
        """
        return self._pub_key

    @pub_key.setter
    def pub_key(self, pub_key: str):
        """Sets the pub_key of this User.


        :param pub_key: The pub_key of this User.
        :type pub_key: str
        """

        self._pub_key = pub_key

    @property
    def tasks_completed(self) -> List[str]:
        """Gets the tasks_completed of this User.

        All the tasks that were completed by the user  # noqa: E501

        :return: The tasks_completed of this User.
        :rtype: List[str]
        """
        return self._tasks_completed

    @tasks_completed.setter
    def tasks_completed(self, tasks_completed: List[str]):
        """Sets the tasks_completed of this User.

        All the tasks that were completed by the user  # noqa: E501

        :param tasks_completed: The tasks_completed of this User.
        :type tasks_completed: List[str]
        """

        self._tasks_completed = tasks_completed

    @property
    def geo_locations(self) -> List[Geolocation]:
        """Gets the geo_locations of this User.

        The array of geolocations registered by the user  # noqa: E501

        :return: The geo_locations of this User.
        :rtype: List[Geolocation]
        """
        return self._geo_locations

    @geo_locations.setter
    def geo_locations(self, geo_locations: List[Geolocation]):
        """Sets the geo_locations of this User.

        The array of geolocations registered by the user  # noqa: E501

        :param geo_locations: The geo_locations of this User.
        :type geo_locations: List[Geolocation]
        """

        self._geo_locations = geo_locations

    @property
    def orders(self) -> List[str]:
        """Gets the orders of this User.

        The array of udids of purchases with vendors  # noqa: E501

        :return: The orders of this User.
        :rtype: List[str]
        """
        return self._orders

    @orders.setter
    def orders(self, orders: List[str]):
        """Sets the orders of this User.

        The array of udids of purchases with vendors  # noqa: E501

        :param orders: The orders of this User.
        :type orders: List[str]
        """

        self._orders = orders
