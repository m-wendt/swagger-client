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


class SaveTVWebApiRequestModelsChannelDeleteRequest(object):
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
        'record_handling': 'int'
    }

    attribute_map = {
        'record_handling': 'recordHandling'
    }

    def __init__(self, record_handling=None):  # noqa: E501
        """SaveTVWebApiRequestModelsChannelDeleteRequest - a model defined in Swagger"""  # noqa: E501

        self._record_handling = None
        self.discriminator = None

        if record_handling is not None:
            self.record_handling = record_handling

    @property
    def record_handling(self):
        """Gets the record_handling of this SaveTVWebApiRequestModelsChannelDeleteRequest.  # noqa: E501


        :return: The record_handling of this SaveTVWebApiRequestModelsChannelDeleteRequest.  # noqa: E501
        :rtype: int
        """
        return self._record_handling

    @record_handling.setter
    def record_handling(self, record_handling):
        """Sets the record_handling of this SaveTVWebApiRequestModelsChannelDeleteRequest.


        :param record_handling: The record_handling of this SaveTVWebApiRequestModelsChannelDeleteRequest.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3]  # noqa: E501
        if record_handling not in allowed_values:
            raise ValueError(
                "Invalid value for `record_handling` ({0}), must be one of {1}"  # noqa: E501
                .format(record_handling, allowed_values)
            )

        self._record_handling = record_handling

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
        if issubclass(SaveTVWebApiRequestModelsChannelDeleteRequest, dict):
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
        if not isinstance(other, SaveTVWebApiRequestModelsChannelDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other