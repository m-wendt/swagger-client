# coding: utf-8

"""
    Save.TV API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.stars__post_api import StarsPostApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStarsPostApi(unittest.TestCase):
    """StarsPostApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.stars__post_api.StarsPostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_stars_post_notification(self):
        """Test case for stars_post_notification

        Creates a subscription for a star notifications (alerts).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
