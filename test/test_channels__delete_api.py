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
from swagger_client.api.channels__delete_api import ChannelsDeleteApi  # noqa: E501
from swagger_client.rest import ApiException


class TestChannelsDeleteApi(unittest.TestCase):
    """ChannelsDeleteApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.channels__delete_api.ChannelsDeleteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_channels_delete(self):
        """Test case for channels_delete

        Deletes the channel with the given identifier.  # noqa: E501
        """
        pass

    def test_channels_delete_all_catch_all_channels(self):
        """Test case for channels_delete_all_catch_all_channels

        Deletes all catch all channels for the current user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
