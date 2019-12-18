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


class SaveTVWebApiResponseModelsChannelTimeFrame(object):
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
        'id': 'int',
        'name': 'str',
        'start_time': 'SaveTVWebApiResponseModelsTime',
        'end_time': 'SaveTVWebApiResponseModelsTime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_time': 'startTime',
        'end_time': 'endTime'
    }

    def __init__(self, id=None, name=None, start_time=None, end_time=None):  # noqa: E501
        """SaveTVWebApiResponseModelsChannelTimeFrame - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501


        :return: The id of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaveTVWebApiResponseModelsChannelTimeFrame.


        :param id: The id of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501


        :return: The name of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTVWebApiResponseModelsChannelTimeFrame.


        :param name: The name of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501


        :return: The start_time of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsTime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SaveTVWebApiResponseModelsChannelTimeFrame.


        :param start_time: The start_time of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :type: SaveTVWebApiResponseModelsTime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501


        :return: The end_time of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsTime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SaveTVWebApiResponseModelsChannelTimeFrame.


        :param end_time: The end_time of this SaveTVWebApiResponseModelsChannelTimeFrame.  # noqa: E501
        :type: SaveTVWebApiResponseModelsTime
        """

        self._end_time = end_time

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
        if issubclass(SaveTVWebApiResponseModelsChannelTimeFrame, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsChannelTimeFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other