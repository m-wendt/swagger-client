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


class SaveTVWebApiRequestModelsRecordFormatFilter(object):
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
        'sort': 'list[OlympCollectionsSortDescription]'
    }

    attribute_map = {
        'sort': 'sort'
    }

    def __init__(self, sort=None):  # noqa: E501
        """SaveTVWebApiRequestModelsRecordFormatFilter - a model defined in Swagger"""  # noqa: E501

        self._sort = None
        self.discriminator = None

        if sort is not None:
            self.sort = sort

    @property
    def sort(self):
        """Gets the sort of this SaveTVWebApiRequestModelsRecordFormatFilter.  # noqa: E501


        :return: The sort of this SaveTVWebApiRequestModelsRecordFormatFilter.  # noqa: E501
        :rtype: list[OlympCollectionsSortDescription]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SaveTVWebApiRequestModelsRecordFormatFilter.


        :param sort: The sort of this SaveTVWebApiRequestModelsRecordFormatFilter.  # noqa: E501
        :type: list[OlympCollectionsSortDescription]
        """

        self._sort = sort

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
        if issubclass(SaveTVWebApiRequestModelsRecordFormatFilter, dict):
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
        if not isinstance(other, SaveTVWebApiRequestModelsRecordFormatFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
