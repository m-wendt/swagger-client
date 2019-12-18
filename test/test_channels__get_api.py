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
from swagger_client.api.channels__get_api import ChannelsGetApi  # noqa: E501
from swagger_client.rest import ApiException


class TestChannelsGetApi(unittest.TestCase):
    """ChannelsGetApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.channels__get_api.ChannelsGetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_channels_count(self):
        """Test case for channels_count

        Retrieves the number of channels for the current account.  # noqa: E501
        """
        pass

    def test_channels_get(self):
        """Test case for channels_get

        Retrieves the channels for the current account.  # noqa: E501
        """
        pass

    def test_channels_get_0(self):
        """Test case for channels_get_0

        Retrieves a single channel with the given identifier.  # noqa: E501
        """
        pass

    def test_channels_telecasts(self):
        """Test case for channels_telecasts

        Retrieves the telecasts that matches the channel criteria.  # noqa: E501
        """
        pass

    def test_channels_telecasts_0(self):
        """Test case for channels_telecasts_0

        Retrieves the telecasts that matches the channel criteria.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
