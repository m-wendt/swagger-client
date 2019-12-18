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
from swagger_client.api.channels__post_api import ChannelsPostApi  # noqa: E501
from swagger_client.rest import ApiException


class TestChannelsPostApi(unittest.TestCase):
    """ChannelsPostApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.channels__post_api.ChannelsPostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_channels_post_catch_all_channel(self):
        """Test case for channels_post_catch_all_channel

        Creates the catch all channels for the requested TV stations or for all TV stations.  # noqa: E501
        """
        pass

    def test_channels_post_full_text_search_channel(self):
        """Test case for channels_post_full_text_search_channel

        Creates a full text search channel.  # noqa: E501
        """
        pass

    def test_channels_post_star_channel(self):
        """Test case for channels_post_star_channel

        Creates a star channel.  # noqa: E501
        """
        pass

    def test_channels_post_telecast_ids_channel(self):
        """Test case for channels_post_telecast_ids_channel

        Creates a channel by various telecast ids.  # noqa: E501
        """
        pass

    def test_channels_post_title_channel(self):
        """Test case for channels_post_title_channel

        Creates a title channel.  # noqa: E501
        """
        pass

    def test_channels_post_tv_station_channel(self):
        """Test case for channels_post_tv_station_channel

        Creates a TV station channel.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
