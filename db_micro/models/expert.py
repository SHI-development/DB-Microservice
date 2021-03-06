# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from db_micro.models.base_model_ import Model
from db_micro.models.expert_geolocation import ExpertGeolocation
from db_micro.models.user import User
from db_micro import util


class Expert(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, first_name: str=None, last_name: str=None, email: str=None, client_id: str=None, geolocation: ExpertGeolocation=None, authored: List[str]=None, category: User=None):  # noqa: E501
        """Expert - a model defined in Swagger

        :param id: The id of this Expert.  # noqa: E501
        :type id: str
        :param first_name: The first_name of this Expert.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Expert.  # noqa: E501
        :type last_name: str
        :param email: The email of this Expert.  # noqa: E501
        :type email: str
        :param client_id: The client_id of this Expert.  # noqa: E501
        :type client_id: str
        :param geolocation: The geolocation of this Expert.  # noqa: E501
        :type geolocation: ExpertGeolocation
        :param authored: The authored of this Expert.  # noqa: E501
        :type authored: List[str]
        :param category: The category of this Expert.  # noqa: E501
        :type category: User
        """
        self.swagger_types = {
            'id': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'client_id': str,
            'geolocation': ExpertGeolocation,
            'authored': List[str],
            'category': User
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'client_id': 'clientId',
            'geolocation': 'geolocation',
            'authored': 'authored',
            'category': 'category'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._client_id = client_id
        self._geolocation = geolocation
        self._authored = authored
        self._category = category

    @classmethod
    def from_dict(cls, dikt) -> 'Expert':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Expert of this Expert.  # noqa: E501
        :rtype: Expert
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Expert.


        :return: The id of this Expert.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Expert.


        :param id: The id of this Expert.
        :type id: str
        """

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Expert.


        :return: The first_name of this Expert.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Expert.


        :param first_name: The first_name of this Expert.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Expert.


        :return: The last_name of this Expert.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Expert.


        :param last_name: The last_name of this Expert.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this Expert.


        :return: The email of this Expert.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Expert.


        :param email: The email of this Expert.
        :type email: str
        """

        self._email = email

    @property
    def client_id(self) -> str:
        """Gets the client_id of this Expert.


        :return: The client_id of this Expert.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Sets the client_id of this Expert.


        :param client_id: The client_id of this Expert.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def geolocation(self) -> ExpertGeolocation:
        """Gets the geolocation of this Expert.


        :return: The geolocation of this Expert.
        :rtype: ExpertGeolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation: ExpertGeolocation):
        """Sets the geolocation of this Expert.


        :param geolocation: The geolocation of this Expert.
        :type geolocation: ExpertGeolocation
        """

        self._geolocation = geolocation

    @property
    def authored(self) -> List[str]:
        """Gets the authored of this Expert.

        All the nodes authored by this expert.  # noqa: E501

        :return: The authored of this Expert.
        :rtype: List[str]
        """
        return self._authored

    @authored.setter
    def authored(self, authored: List[str]):
        """Sets the authored of this Expert.

        All the nodes authored by this expert.  # noqa: E501

        :param authored: The authored of this Expert.
        :type authored: List[str]
        """

        self._authored = authored

    @property
    def category(self) -> User:
        """Gets the category of this Expert.


        :return: The category of this Expert.
        :rtype: User
        """
        return self._category

    @category.setter
    def category(self, category: User):
        """Sets the category of this Expert.


        :param category: The category of this Expert.
        :type category: User
        """

        self._category = category
