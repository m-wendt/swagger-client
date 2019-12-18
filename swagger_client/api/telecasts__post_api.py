# coding: utf-8

"""
    Save.TV API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TelecastsPostApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def telecasts_rating(self, id, telecast_rating, **kwargs):  # noqa: E501
        """Ratings the specified identifier.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.telecasts_rating(id, telecast_rating, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier. (required)
        :param SaveTVWebApiRequestModelsTelecastRating telecast_rating: The rating for the telecast. The allowed range for the rating is between 1 and 5. (required)
        :return: SaveTVEpgTelecastsRating
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.telecasts_rating_with_http_info(id, telecast_rating, **kwargs)  # noqa: E501
        else:
            (data) = self.telecasts_rating_with_http_info(id, telecast_rating, **kwargs)  # noqa: E501
            return data

    def telecasts_rating_with_http_info(self, id, telecast_rating, **kwargs):  # noqa: E501
        """Ratings the specified identifier.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.telecasts_rating_with_http_info(id, telecast_rating, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier. (required)
        :param SaveTVWebApiRequestModelsTelecastRating telecast_rating: The rating for the telecast. The allowed range for the rating is between 1 and 5. (required)
        :return: SaveTVEpgTelecastsRating
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'telecast_rating']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method telecasts_rating" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `telecasts_rating`")  # noqa: E501
        # verify the required parameter 'telecast_rating' is set
        if ('telecast_rating' not in params or
                params['telecast_rating'] is None):
            raise ValueError("Missing the required parameter `telecast_rating` when calling `telecasts_rating`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'telecast_rating' in params:
            body_params = params['telecast_rating']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v3/telecasts/{id}/rating', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SaveTVEpgTelecastsRating',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)