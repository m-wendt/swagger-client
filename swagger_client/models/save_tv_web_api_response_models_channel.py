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


class SaveTVWebApiResponseModelsChannel(object):
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
        'channel_type': 'int',
        'count_telecasts': 'int',
        'image_url100': 'str',
        'image_url250': 'str',
        'image_url500': 'str',
        'channel_scope': 'int',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'channel_type': 'channelType',
        'count_telecasts': 'countTelecasts',
        'image_url100': 'imageUrl100',
        'image_url250': 'imageUrl250',
        'image_url500': 'imageUrl500',
        'channel_scope': 'channelScope',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, channel_type=None, count_telecasts=None, image_url100=None, image_url250=None, image_url500=None, channel_scope=None, id=None, name=None):  # noqa: E501
        """SaveTVWebApiResponseModelsChannel - a model defined in Swagger"""  # noqa: E501

        self._channel_type = None
        self._count_telecasts = None
        self._image_url100 = None
        self._image_url250 = None
        self._image_url500 = None
        self._channel_scope = None
        self._id = None
        self._name = None
        self.discriminator = None

        if channel_type is not None:
            self.channel_type = channel_type
        if count_telecasts is not None:
            self.count_telecasts = count_telecasts
        if image_url100 is not None:
            self.image_url100 = image_url100
        if image_url250 is not None:
            self.image_url250 = image_url250
        if image_url500 is not None:
            self.image_url500 = image_url500
        if channel_scope is not None:
            self.channel_scope = channel_scope
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def channel_type(self):
        """Gets the channel_type of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The channel_type of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: int
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this SaveTVWebApiResponseModelsChannel.


        :param channel_type: The channel_type of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :type: int
        """

        self._channel_type = channel_type

    @property
    def count_telecasts(self):
        """Gets the count_telecasts of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The count_telecasts of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: int
        """
        return self._count_telecasts

    @count_telecasts.setter
    def count_telecasts(self, count_telecasts):
        """Sets the count_telecasts of this SaveTVWebApiResponseModelsChannel.


        :param count_telecasts: The count_telecasts of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :type: int
        """

        self._count_telecasts = count_telecasts

    @property
    def image_url100(self):
        """Gets the image_url100 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The image_url100 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: str
        """
        return self._image_url100

    @image_url100.setter
    def image_url100(self, image_url100):
        """Sets the image_url100 of this SaveTVWebApiResponseModelsChannel.


        :param image_url100: The image_url100 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :type: str
        """

        self._image_url100 = image_url100

    @property
    def image_url250(self):
        """Gets the image_url250 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The image_url250 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: str
        """
        return self._image_url250

    @image_url250.setter
    def image_url250(self, image_url250):
        """Sets the image_url250 of this SaveTVWebApiResponseModelsChannel.


        :param image_url250: The image_url250 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :type: str
        """

        self._image_url250 = image_url250

    @property
    def image_url500(self):
        """Gets the image_url500 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The image_url500 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: str
        """
        return self._image_url500

    @image_url500.setter
    def image_url500(self, image_url500):
        """Sets the image_url500 of this SaveTVWebApiResponseModelsChannel.


        :param image_url500: The image_url500 of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :type: str
        """

        self._image_url500 = image_url500

    @property
    def channel_scope(self):
        """Gets the channel_scope of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The channel_scope of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: int
        """
        return self._channel_scope

    @channel_scope.setter
    def channel_scope(self, channel_scope):
        """Sets the channel_scope of this SaveTVWebApiResponseModelsChannel.


        :param channel_scope: The channel_scope of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :type: int
        """

        self._channel_scope = channel_scope

    @property
    def id(self):
        """Gets the id of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The id of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaveTVWebApiResponseModelsChannel.


        :param id: The id of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SaveTVWebApiResponseModelsChannel.  # noqa: E501


        :return: The name of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTVWebApiResponseModelsChannel.


        :param name: The name of this SaveTVWebApiResponseModelsChannel.  # noqa: E501
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
        if issubclass(SaveTVWebApiResponseModelsChannel, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
