import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_enhanced_user(clientId, firstName, lastName, email, address=None):  # noqa: E501
    """Add an enhanced user

     # noqa: E501

    :param clientId: Client ID of enhanced user
    :type clientId: str
    :param firstName: First name of enhanced user
    :type firstName: str
    :param lastName: Last name of enhanced user
    :type lastName: str
    :param email: Email of enhanced user
    :type email: str
    :param address: The physical address of the enhanced user
    :type address: str

    :rtype: None
    """
    return 'do some magic!'


def create_user(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: Create user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(userId):  # noqa: E501
    """Delete user

     # noqa: E501

    :param userId: 
    :type userId: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_id(userId):  # noqa: E501
    """Get user by user ID

    Get user anonymous info by ID # noqa: E501

    :param userId: 
    :type userId: str

    :rtype: User
    """
    return 'do some magic!'


def update_user(userId, body):  # noqa: E501
    """Update a user by user ID

    Send Ananymous user data by user ID # noqa: E501

    :param userId: 
    :type userId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
