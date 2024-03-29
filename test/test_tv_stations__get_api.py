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
from swagger_client.api.tv_stations__get_api import TvStationsGetApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTvStationsGetApi(unittest.TestCase):
    """TvStationsGetApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tv_stations__get_api.TvStationsGetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tv_stations_get(self):
        """Test case for tv_stations_get

        Retrieves all available TV stations.  # noqa: E501
        """
        pass

    def test_tv_stations_get_0(self):
        """Test case for tv_stations_get_0

        Retrieves a single TV station with the given identifier.  # noqa: E501
        """
        pass

    def test_tv_stations_live_stream_live_stream_urls(self):
        """Test case for tv_stations_live_stream_live_stream_urls

        Returns the live streaming url for the given TV station in all possible formats.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
