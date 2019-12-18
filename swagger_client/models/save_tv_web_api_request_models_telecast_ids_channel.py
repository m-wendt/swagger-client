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


class SaveTVWebApiRequestModelsTelecastIdsChannel(object):
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
        'list_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'list_id': 'listId',
        'name': 'name'
    }

    def __init__(self, list_id=None, name=None):  # noqa: E501
        """SaveTVWebApiRequestModelsTelecastIdsChannel - a model defined in Swagger"""  # noqa: E501

        self._list_id = None
        self._name = None
        self.discriminator = None

        if list_id is not None:
            self.list_id = list_id
        if name is not None:
            self.name = name

    @property
    def list_id(self):
        """Gets the list_id of this SaveTVWebApiRequestModelsTelecastIdsChannel.  # noqa: E501


        :return: The list_id of this SaveTVWebApiRequestModelsTelecastIdsChannel.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this SaveTVWebApiRequestModelsTelecastIdsChannel.


        :param list_id: The list_id of this SaveTVWebApiRequestModelsTelecastIdsChannel.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def name(self):
        """Gets the name of this SaveTVWebApiRequestModelsTelecastIdsChannel.  # noqa: E501


        :return: The name of this SaveTVWebApiRequestModelsTelecastIdsChannel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTVWebApiRequestModelsTelecastIdsChannel.


        :param name: The name of this SaveTVWebApiRequestModelsTelecastIdsChannel.  # noqa: E501
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
        if issubclass(SaveTVWebApiRequestModelsTelecastIdsChannel, dict):
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
        if not isinstance(other, SaveTVWebApiRequestModelsTelecastIdsChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
