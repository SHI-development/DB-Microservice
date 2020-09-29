import connexion
import six

from db_micro.models.server_error import ServerError  # noqa: E501
from db_micro.models.yogi import Yogi  # noqa: E501
from db_micro import util


def create_yogi(body):  # noqa: E501
    """Create yogi

     # noqa: E501

    :param body: Create Yogi object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Yogi.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_yogi(yogiId):  # noqa: E501
    """Delete yogi

     # noqa: E501

    :param yogiId: 
    :type yogiId: str

    :rtype: None
    """
    return 'do some magic!'


def get_yogi_by_id(yogiId):  # noqa: E501
    """Get yogi by yogi ID

    Get user anonymous info by ID # noqa: E501

    :param yogiId: 
    :type yogiId: str

    :rtype: Yogi
    """
    return 'do some magic!'


def suggest_yogi(userId):  # noqa: E501
    """Suggest a yogi based on user characteristics

     # noqa: E501

    :param userId: 
    :type userId: str

    :rtype: Yogi
    """
    return 'do some magic!'


def update_yogi(yogiId, body):  # noqa: E501
    """Update a yogi

     # noqa: E501

    :param yogiId: 
    :type yogiId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Yogi.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
