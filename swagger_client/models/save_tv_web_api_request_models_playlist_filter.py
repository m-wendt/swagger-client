# coding: utf-8

"""
    Save.TV API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SaveTVWebApiRequestModelsPlaylistFilter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sort': 'list[OlympCollectionsSortDescription]',
        'playlist_ids': 'list[int]',
        'is_public': 'bool',
        'playlist_types': 'list[int]',
        'fields': 'list[str]'
    }

    attribute_map = {
        'sort': 'sort',
        'playlist_ids': 'playlistIds',
        'is_public': 'isPublic',
        'playlist_types': 'playlistTypes',
        'fields': 'fields'
    }

    def __init__(self, sort=None, playlist_ids=None, is_public=None, playlist_types=None, fields=None):  # noqa: E501
        """SaveTVWebApiRequestModelsPlaylistFilter - a model defined in Swagger"""  # noqa: E501

        self._sort = None
        self._playlist_ids = None
        self._is_public = None
        self._playlist_types = None
        self._fields = None
        self.discriminator = None

        if sort is not None:
            self.sort = sort
        if playlist_ids is not None:
            self.playlist_ids = playlist_ids
        if is_public is not None:
            self.is_public = is_public
        if playlist_types is not None:
            self.playlist_types = playlist_types
        if fields is not None:
            self.fields = fields

    @property
    def sort(self):
        """Gets the sort of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501


        :return: The sort of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :rtype: list[OlympCollectionsSortDescription]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SaveTVWebApiRequestModelsPlaylistFilter.


        :param sort: The sort of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :type: list[OlympCollectionsSortDescription]
        """

        self._sort = sort

    @property
    def playlist_ids(self):
        """Gets the playlist_ids of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501


        :return: The playlist_ids of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._playlist_ids

    @playlist_ids.setter
    def playlist_ids(self, playlist_ids):
        """Sets the playlist_ids of this SaveTVWebApiRequestModelsPlaylistFilter.


        :param playlist_ids: The playlist_ids of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :type: list[int]
        """

        self._playlist_ids = playlist_ids

    @property
    def is_public(self):
        """Gets the is_public of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501


        :return: The is_public of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this SaveTVWebApiRequestModelsPlaylistFilter.


        :param is_public: The is_public of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def playlist_types(self):
        """Gets the playlist_types of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501


        :return: The playlist_types of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._playlist_types

    @playlist_types.setter
    def playlist_types(self, playlist_types):
        """Sets the playlist_types of this SaveTVWebApiRequestModelsPlaylistFilter.


        :param playlist_types: The playlist_types of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :type: list[int]
        """

        self._playlist_types = playlist_types

    @property
    def fields(self):
        """Gets the fields of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501


        :return: The fields of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this SaveTVWebApiRequestModelsPlaylistFilter.


        :param fields: The fields of this SaveTVWebApiRequestModelsPlaylistFilter.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SaveTVWebApiRequestModelsPlaylistFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SaveTVWebApiRequestModelsPlaylistFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
