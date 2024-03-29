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


class SaveTVWebApiResponseModelsRecord(object):
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
        'start_date': 'datetime',
        'end_date': 'datetime',
        'create_date': 'datetime',
        'update_date': 'datetime',
        'is_ad_cut_enabled': 'bool',
        'ad_free_available': 'bool',
        'ad_free_length': 'int',
        'formats': 'list[SaveTVWebApiResponseModelsRecordRequestedFormat]',
        'channels': 'list[SaveTVWebApiResponseModelsChannelBase]',
        'telecast': 'SaveTVWebApiResponseModelsTelecast',
        'defect': 'SaveTVWebApiResponseModelsRecordDefect',
        'tags': 'list[SaveTVWebApiResponseModelsTag]',
        'playlists': 'list[SaveTVWebApiResponseModelsPlaylistBase]',
        'resume_positions': 'SaveTVWebApiResponseModelsResumePositions'
    }

    attribute_map = {
        'telecast_id': 'telecastId',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'create_date': 'createDate',
        'update_date': 'updateDate',
        'is_ad_cut_enabled': 'isAdCutEnabled',
        'ad_free_available': 'adFreeAvailable',
        'ad_free_length': 'adFreeLength',
        'formats': 'formats',
        'channels': 'channels',
        'telecast': 'telecast',
        'defect': 'defect',
        'tags': 'tags',
        'playlists': 'playlists',
        'resume_positions': 'resumePositions'
    }

    def __init__(self, telecast_id=None, start_date=None, end_date=None, create_date=None, update_date=None, is_ad_cut_enabled=None, ad_free_available=None, ad_free_length=None, formats=None, channels=None, telecast=None, defect=None, tags=None, playlists=None, resume_positions=None):  # noqa: E501
        """SaveTVWebApiResponseModelsRecord - a model defined in Swagger"""  # noqa: E501

        self._telecast_id = None
        self._start_date = None
        self._end_date = None
        self._create_date = None
        self._update_date = None
        self._is_ad_cut_enabled = None
        self._ad_free_available = None
        self._ad_free_length = None
        self._formats = None
        self._channels = None
        self._telecast = None
        self._defect = None
        self._tags = None
        self._playlists = None
        self._resume_positions = None
        self.discriminator = None

        if telecast_id is not None:
            self.telecast_id = telecast_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if create_date is not None:
            self.create_date = create_date
        if update_date is not None:
            self.update_date = update_date
        if is_ad_cut_enabled is not None:
            self.is_ad_cut_enabled = is_ad_cut_enabled
        if ad_free_available is not None:
            self.ad_free_available = ad_free_available
        if ad_free_length is not None:
            self.ad_free_length = ad_free_length
        if formats is not None:
            self.formats = formats
        if channels is not None:
            self.channels = channels
        if telecast is not None:
            self.telecast = telecast
        if defect is not None:
            self.defect = defect
        if tags is not None:
            self.tags = tags
        if playlists is not None:
            self.playlists = playlists
        if resume_positions is not None:
            self.resume_positions = resume_positions

    @property
    def telecast_id(self):
        """Gets the telecast_id of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The telecast_id of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: int
        """
        return self._telecast_id

    @telecast_id.setter
    def telecast_id(self, telecast_id):
        """Sets the telecast_id of this SaveTVWebApiResponseModelsRecord.


        :param telecast_id: The telecast_id of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: int
        """

        self._telecast_id = telecast_id

    @property
    def start_date(self):
        """Gets the start_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The start_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SaveTVWebApiResponseModelsRecord.


        :param start_date: The start_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The end_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SaveTVWebApiResponseModelsRecord.


        :param end_date: The end_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def create_date(self):
        """Gets the create_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The create_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this SaveTVWebApiResponseModelsRecord.


        :param create_date: The create_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def update_date(self):
        """Gets the update_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The update_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this SaveTVWebApiResponseModelsRecord.


        :param update_date: The update_date of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def is_ad_cut_enabled(self):
        """Gets the is_ad_cut_enabled of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The is_ad_cut_enabled of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: bool
        """
        return self._is_ad_cut_enabled

    @is_ad_cut_enabled.setter
    def is_ad_cut_enabled(self, is_ad_cut_enabled):
        """Sets the is_ad_cut_enabled of this SaveTVWebApiResponseModelsRecord.


        :param is_ad_cut_enabled: The is_ad_cut_enabled of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: bool
        """

        self._is_ad_cut_enabled = is_ad_cut_enabled

    @property
    def ad_free_available(self):
        """Gets the ad_free_available of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The ad_free_available of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: bool
        """
        return self._ad_free_available

    @ad_free_available.setter
    def ad_free_available(self, ad_free_available):
        """Sets the ad_free_available of this SaveTVWebApiResponseModelsRecord.


        :param ad_free_available: The ad_free_available of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: bool
        """

        self._ad_free_available = ad_free_available

    @property
    def ad_free_length(self):
        """Gets the ad_free_length of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The ad_free_length of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: int
        """
        return self._ad_free_length

    @ad_free_length.setter
    def ad_free_length(self, ad_free_length):
        """Sets the ad_free_length of this SaveTVWebApiResponseModelsRecord.


        :param ad_free_length: The ad_free_length of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: int
        """

        self._ad_free_length = ad_free_length

    @property
    def formats(self):
        """Gets the formats of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The formats of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: list[SaveTVWebApiResponseModelsRecordRequestedFormat]
        """
        return self._formats

    @formats.setter
    def formats(self, formats):
        """Sets the formats of this SaveTVWebApiResponseModelsRecord.


        :param formats: The formats of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: list[SaveTVWebApiResponseModelsRecordRequestedFormat]
        """

        self._formats = formats

    @property
    def channels(self):
        """Gets the channels of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The channels of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: list[SaveTVWebApiResponseModelsChannelBase]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this SaveTVWebApiResponseModelsRecord.


        :param channels: The channels of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: list[SaveTVWebApiResponseModelsChannelBase]
        """

        self._channels = channels

    @property
    def telecast(self):
        """Gets the telecast of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The telecast of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsTelecast
        """
        return self._telecast

    @telecast.setter
    def telecast(self, telecast):
        """Sets the telecast of this SaveTVWebApiResponseModelsRecord.


        :param telecast: The telecast of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: SaveTVWebApiResponseModelsTelecast
        """

        self._telecast = telecast

    @property
    def defect(self):
        """Gets the defect of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The defect of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsRecordDefect
        """
        return self._defect

    @defect.setter
    def defect(self, defect):
        """Sets the defect of this SaveTVWebApiResponseModelsRecord.


        :param defect: The defect of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: SaveTVWebApiResponseModelsRecordDefect
        """

        self._defect = defect

    @property
    def tags(self):
        """Gets the tags of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The tags of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: list[SaveTVWebApiResponseModelsTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SaveTVWebApiResponseModelsRecord.


        :param tags: The tags of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: list[SaveTVWebApiResponseModelsTag]
        """

        self._tags = tags

    @property
    def playlists(self):
        """Gets the playlists of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The playlists of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: list[SaveTVWebApiResponseModelsPlaylistBase]
        """
        return self._playlists

    @playlists.setter
    def playlists(self, playlists):
        """Sets the playlists of this SaveTVWebApiResponseModelsRecord.


        :param playlists: The playlists of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: list[SaveTVWebApiResponseModelsPlaylistBase]
        """

        self._playlists = playlists

    @property
    def resume_positions(self):
        """Gets the resume_positions of this SaveTVWebApiResponseModelsRecord.  # noqa: E501


        :return: The resume_positions of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :rtype: SaveTVWebApiResponseModelsResumePositions
        """
        return self._resume_positions

    @resume_positions.setter
    def resume_positions(self, resume_positions):
        """Sets the resume_positions of this SaveTVWebApiResponseModelsRecord.


        :param resume_positions: The resume_positions of this SaveTVWebApiResponseModelsRecord.  # noqa: E501
        :type: SaveTVWebApiResponseModelsResumePositions
        """

        self._resume_positions = resume_positions

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
        if issubclass(SaveTVWebApiResponseModelsRecord, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
