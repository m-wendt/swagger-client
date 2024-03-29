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


class SaveTVWebApiResponseModelsTvStation(object):
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
        'small_logo_url': 'str',
        'large_logo_url': 'str',
        'homepage_url': 'str',
        'is_recordable': 'bool',
        'live_stream': 'SaveTVWebApiResponseModelsTvStationLiveStream'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'small_logo_url': 'smallLogoUrl',
        'large_logo_url': 'largeLogoUrl',
        'homepage_url': 'homepageUrl',
        'is_recordable': 'isRecordable',
        'live_stream': 'liveStream'
    }

    def __init__(self, id=None, name=None, small_logo_url=None, large_logo_url=None, homepage_url=None, is_recordable=None, live_stream=None):  # noqa: E501
        """SaveTVWebApiResponseModelsTvStation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._small_logo_url = None
        self._large_logo_url = None
        self._homepage_url = None
        self._is_recordable = None
        self._live_stream = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if small_logo_url is not None:
            self.small_logo_url = small_logo_url
        if large_logo_url is not None:
            self.large_logo_url = large_logo_url
        if homepage_url is not None:
            self.homepage_url = homepage_url
        if is_recordable is not None:
            self.is_recordable = is_recordable
        if live_stream is not None:
            self.live_stream = live_stream

    @property
    def id(self):
        """Gets the id of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501


        :return: The id of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaveTVWebApiResponseModelsTvStation.


        :param id: The id of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501


        :return: The name of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTVWebApiResponseModelsTvStation.


        :param name: The name of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def small_logo_url(self):
        """Gets the small_logo_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501


        :return: The small_logo_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :rtype: str
        """
        return self._small_logo_url

    @small_logo_url.setter
    def small_logo_url(self, small_logo_url):
        """Sets the small_logo_url of this SaveTVWebApiResponseModelsTvStation.


        :param small_logo_url: The small_logo_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :type: str
        """

        self._small_logo_url = small_logo_url

    @property
    def large_logo_url(self):
        """Gets the large_logo_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501


        :return: The large_logo_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :rtype: str
        """
        return self._large_logo_url

    @large_logo_url.setter
    def large_logo_url(self, large_logo_url):
        """Sets the large_logo_url of this SaveTVWebApiResponseModelsTvStation.


        :param large_logo_url: The large_logo_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :type: str
        """

        self._large_logo_url = large_logo_url

    @property
    def homepage_url(self):
        """Gets the homepage_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501


        :return: The homepage_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :rtype: str
        """
        return self._homepage_url

    @homepage_url.setter
    def homepage_url(self, homepage_url):
        """Sets the homepage_url of this SaveTVWebApiResponseModelsTvStation.


        :param homepage_url: The homepage_url of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :type: str
        """

        self._homepage_url = homepage_url

    @property
    def is_recordable(self):
        """Gets the is_recordable of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501


        :return: The is_recordable of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :rtype: bool
        """
        return self._is_recordable

    @is_recordable.setter
    def is_recordable(self, is_recordable):
        """Sets the is_recordable of this SaveTVWebApiResponseModelsTvStation.


        :param is_recordable: The is_recordable of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :type: bool
        """

        self._is_recordable = is_recordable

    @property
    def live_stream(self):
        """Gets the live_stream of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501


        :return: The live_stream of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsTvStationLiveStream
        """
        return self._live_stream

    @live_stream.setter
    def live_stream(self, live_stream):
        """Sets the live_stream of this SaveTVWebApiResponseModelsTvStation.


        :param live_stream: The live_stream of this SaveTVWebApiResponseModelsTvStation.  # noqa: E501
        :type: SaveTVWebApiResponseModelsTvStationLiveStream
        """

        self._live_stream = live_stream

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
        if issubclass(SaveTVWebApiResponseModelsTvStation, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsTvStation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
