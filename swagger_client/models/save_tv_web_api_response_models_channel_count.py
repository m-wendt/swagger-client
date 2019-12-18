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


class SaveTVWebApiResponseModelsChannelCount(object):
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
        'count': 'int',
        'count_catch_all': 'int',
        'allowed': 'int'
    }

    attribute_map = {
        'count': 'count',
        'count_catch_all': 'countCatchAll',
        'allowed': 'allowed'
    }

    def __init__(self, count=None, count_catch_all=None, allowed=None):  # noqa: E501
        """SaveTVWebApiResponseModelsChannelCount - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._count_catch_all = None
        self._allowed = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if count_catch_all is not None:
            self.count_catch_all = count_catch_all
        if allowed is not None:
            self.allowed = allowed

    @property
    def count(self):
        """Gets the count of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501


        :return: The count of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SaveTVWebApiResponseModelsChannelCount.


        :param count: The count of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def count_catch_all(self):
        """Gets the count_catch_all of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501


        :return: The count_catch_all of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501
        :rtype: int
        """
        return self._count_catch_all

    @count_catch_all.setter
    def count_catch_all(self, count_catch_all):
        """Sets the count_catch_all of this SaveTVWebApiResponseModelsChannelCount.


        :param count_catch_all: The count_catch_all of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501
        :type: int
        """

        self._count_catch_all = count_catch_all

    @property
    def allowed(self):
        """Gets the allowed of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501


        :return: The allowed of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501
        :rtype: int
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this SaveTVWebApiResponseModelsChannelCount.


        :param allowed: The allowed of this SaveTVWebApiResponseModelsChannelCount.  # noqa: E501
        :type: int
        """

        self._allowed = allowed

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
        if issubclass(SaveTVWebApiResponseModelsChannelCount, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsChannelCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
