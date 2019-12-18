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


class SaveTVWebApiResponseModelsPlaylistItem(object):
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
        'telecast_id': 'int',
        'full_title': 'str',
        'record': 'SaveTVWebApiResponseModelsRecord',
        'telecast': 'SaveTVWebApiResponseModelsTelecast'
    }

    attribute_map = {
        'telecast_id': 'telecastId',
        'full_title': 'fullTitle',
        'record': 'record',
        'telecast': 'telecast'
    }

    def __init__(self, telecast_id=None, full_title=None, record=None, telecast=None):  # noqa: E501
        """SaveTVWebApiResponseModelsPlaylistItem - a model defined in Swagger"""  # noqa: E501

        self._telecast_id = None
        self._full_title = None
        self._record = None
        self._telecast = None
        self.discriminator = None

        if telecast_id is not None:
            self.telecast_id = telecast_id
        if full_title is not None:
            self.full_title = full_title
        if record is not None:
            self.record = record
        if telecast is not None:
            self.telecast = telecast

    @property
    def telecast_id(self):
        """Gets the telecast_id of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501


        :return: The telecast_id of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :rtype: int
        """
        return self._telecast_id

    @telecast_id.setter
    def telecast_id(self, telecast_id):
        """Sets the telecast_id of this SaveTVWebApiResponseModelsPlaylistItem.


        :param telecast_id: The telecast_id of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :type: int
        """

        self._telecast_id = telecast_id

    @property
    def full_title(self):
        """Gets the full_title of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501


        :return: The full_title of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :rtype: str
        """
        return self._full_title

    @full_title.setter
    def full_title(self, full_title):
        """Sets the full_title of this SaveTVWebApiResponseModelsPlaylistItem.


        :param full_title: The full_title of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :type: str
        """

        self._full_title = full_title

    @property
    def record(self):
        """Gets the record of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501


        :return: The record of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this SaveTVWebApiResponseModelsPlaylistItem.


        :param record: The record of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :type: SaveTVWebApiResponseModelsRecord
        """

        self._record = record

    @property
    def telecast(self):
        """Gets the telecast of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501


        :return: The telecast of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsTelecast
        """
        return self._telecast

    @telecast.setter
    def telecast(self, telecast):
        """Sets the telecast of this SaveTVWebApiResponseModelsPlaylistItem.


        :param telecast: The telecast of this SaveTVWebApiResponseModelsPlaylistItem.  # noqa: E501
        :type: SaveTVWebApiResponseModelsTelecast
        """

        self._telecast = telecast

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
        if issubclass(SaveTVWebApiResponseModelsPlaylistItem, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsPlaylistItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other