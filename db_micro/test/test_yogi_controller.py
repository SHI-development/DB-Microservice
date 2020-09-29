# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from db_micro.models.server_error import ServerError  # noqa: E501
from db_micro.models.yogi import Yogi  # noqa: E501
from db_micro.test import BaseTestCase


class TestYogiController(BaseTestCase):
    """YogiController integration test stubs"""

    def test_create_yogi(self):
        """Test case for create_yogi

        Create yogi
        """
        body = Yogi()
        response = self.client.open(
            '/yogi',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_yogi(self):
        """Test case for delete_yogi

        Delete yogi
        """
        response = self.client.open(
            '/yogi/{yogiId}'.format(yogiId='yogiId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_yogi_by_id(self):
        """Test case for get_yogi_by_id

        Get yogi by yogi ID
        """
        response = self.client.open(
            '/yogi/{yogiId}'.format(yogiId='yogiId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suggest_yogi(self):
        """Test case for suggest_yogi

        Suggest a yogi based on user characteristics
        """
        response = self.client.open(
            '/suggest/{userId}'.format(userId='userId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_yogi(self):
        """Test case for update_yogi

        Update a yogi
        """
        body = Yogi()
        response = self.client.open(
            '/yogi/{yogiId}'.format(yogiId='yogiId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
