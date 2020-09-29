# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from db_micro.models.expert import Expert  # noqa: E501
from db_micro.test import BaseTestCase


class TestExpertController(BaseTestCase):
    """ExpertController integration test stubs"""

    def test_create_expert(self):
        """Test case for create_expert

        Create an expert
        """
        body = Expert()
        response = self.client.open(
            '/expert',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
