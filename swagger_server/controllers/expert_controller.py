import connexion
import six

from swagger_server.models.expert import Expert  # noqa: E501
from swagger_server import util


def create_expert(body):  # noqa: E501
    """Create an expert

     # noqa: E501

    :param body: Create Expert object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Expert.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
