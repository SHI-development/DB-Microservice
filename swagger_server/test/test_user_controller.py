# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_enhanced_user(self):
        """Test case for create_enhanced_user

        Add an enhanced user
        """
        data = dict(firstName='firstName_example',
                    lastName='lastName_example',
                    email='email_example',
                    address='address_example')
        response = self.client.open(
            '/enhancedUser/{clientId}'.format(clientId='clientId_example'),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        body = User()
        response = self.client.open(
            '/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            '/user/{userId}'.format(userId='userId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Get user by user ID
        """
        response = self.client.open(
            '/user/{userId}'.format(userId='userId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Update a user by user ID
        """
        body = User()
        response = self.client.open(
            '/user/{userId}'.format(userId='userId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
