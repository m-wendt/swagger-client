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


class SaveTVWebApiRequestModelsCatchAllChannel(object):
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
        'tv_station_ids': 'list[int]',
        'fields': 'list[str]'
    }

    attribute_map = {
        'tv_station_ids': 'tvStationIds',
        'fields': 'fields'
    }

    def __init__(self, tv_station_ids=None, fields=None):  # noqa: E501
        """SaveTVWebApiRequestModelsCatchAllChannel - a model defined in Swagger"""  # noqa: E501

        self._tv_station_ids = None
        self._fields = None
        self.discriminator = None

        if tv_station_ids is not None:
            self.tv_station_ids = tv_station_ids
        if fields is not None:
            self.fields = fields

    @property
    def tv_station_ids(self):
        """Gets the tv_station_ids of this SaveTVWebApiRequestModelsCatchAllChannel.  # noqa: E501


        :return: The tv_station_ids of this SaveTVWebApiRequestModelsCatchAllChannel.  # noqa: E501
        :rtype: list[int]
        """
        return self._tv_station_ids

    @tv_station_ids.setter
    def tv_station_ids(self, tv_station_ids):
        """Sets the tv_station_ids of this SaveTVWebApiRequestModelsCatchAllChannel.


        :param tv_station_ids: The tv_station_ids of this SaveTVWebApiRequestModelsCatchAllChannel.  # noqa: E501
        :type: list[int]
        """

        self._tv_station_ids = tv_station_ids

    @property
    def fields(self):
        """Gets the fields of this SaveTVWebApiRequestModelsCatchAllChannel.  # noqa: E501


        :return: The fields of this SaveTVWebApiRequestModelsCatchAllChannel.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this SaveTVWebApiRequestModelsCatchAllChannel.


        :param fields: The fields of this SaveTVWebApiRequestModelsCatchAllChannel.  # noqa: E501
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
        if issubclass(SaveTVWebApiRequestModelsCatchAllChannel, dict):
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
        if not isinstance(other, SaveTVWebApiRequestModelsCatchAllChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
