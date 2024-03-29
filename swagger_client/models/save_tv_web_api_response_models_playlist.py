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


class SaveTVWebApiResponseModelsPlaylist(object):
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
        'is_public': 'bool',
        'playlist_type': 'int',
        'items_count': 'int',
        'last_telecast_id': 'int',
        'items': 'list[SaveTVWebApiResponseModelsPlaylistItem]',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'is_public': 'isPublic',
        'playlist_type': 'playlistType',
        'items_count': 'itemsCount',
        'last_telecast_id': 'lastTelecastId',
        'items': 'items',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, is_public=None, playlist_type=None, items_count=None, last_telecast_id=None, items=None, id=None, name=None):  # noqa: E501
        """SaveTVWebApiResponseModelsPlaylist - a model defined in Swagger"""  # noqa: E501

        self._is_public = None
        self._playlist_type = None
        self._items_count = None
        self._last_telecast_id = None
        self._items = None
        self._id = None
        self._name = None
        self.discriminator = None

        if is_public is not None:
            self.is_public = is_public
        if playlist_type is not None:
            self.playlist_type = playlist_type
        if items_count is not None:
            self.items_count = items_count
        if last_telecast_id is not None:
            self.last_telecast_id = last_telecast_id
        if items is not None:
            self.items = items
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def is_public(self):
        """Gets the is_public of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501


        :return: The is_public of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this SaveTVWebApiResponseModelsPlaylist.


        :param is_public: The is_public of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def playlist_type(self):
        """Gets the playlist_type of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501


        :return: The playlist_type of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :rtype: int
        """
        return self._playlist_type

    @playlist_type.setter
    def playlist_type(self, playlist_type):
        """Sets the playlist_type of this SaveTVWebApiResponseModelsPlaylist.


        :param playlist_type: The playlist_type of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :type: int
        """

        self._playlist_type = playlist_type

    @property
    def items_count(self):
        """Gets the items_count of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501


        :return: The items_count of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :rtype: int
        """
        return self._items_count

    @items_count.setter
    def items_count(self, items_count):
        """Sets the items_count of this SaveTVWebApiResponseModelsPlaylist.


        :param items_count: The items_count of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :type: int
        """

        self._items_count = items_count

    @property
    def last_telecast_id(self):
        """Gets the last_telecast_id of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501


        :return: The last_telecast_id of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :rtype: int
        """
        return self._last_telecast_id

    @last_telecast_id.setter
    def last_telecast_id(self, last_telecast_id):
        """Sets the last_telecast_id of this SaveTVWebApiResponseModelsPlaylist.


        :param last_telecast_id: The last_telecast_id of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :type: int
        """

        self._last_telecast_id = last_telecast_id

    @property
    def items(self):
        """Gets the items of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501


        :return: The items of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :rtype: list[SaveTVWebApiResponseModelsPlaylistItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SaveTVWebApiResponseModelsPlaylist.


        :param items: The items of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :type: list[SaveTVWebApiResponseModelsPlaylistItem]
        """

        self._items = items

    @property
    def id(self):
        """Gets the id of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501


        :return: The id of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaveTVWebApiResponseModelsPlaylist.


        :param id: The id of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501


        :return: The name of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTVWebApiResponseModelsPlaylist.


        :param name: The name of this SaveTVWebApiResponseModelsPlaylist.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(SaveTVWebApiResponseModelsPlaylist, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsPlaylist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
