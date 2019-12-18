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
from swagger_client.api.tv_categories__get_api import TvCategoriesGetApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTvCategoriesGetApi(unittest.TestCase):
    """TvCategoriesGetApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tv_categories__get_api.TvCategoriesGetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tv_categories_get(self):
        """Test case for tv_categories_get

        Retrieves all available TV categories.  # noqa: E501
        """
        pass

    def test_tv_categories_get_0(self):
        """Test case for tv_categories_get_0

        Retrieves a single TV category with the given identifier.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
