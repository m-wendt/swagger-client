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


class SaveTVWebApiRequestModelsRecordCountFilter(object):
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
        'ad_free_available': 'bool',
        'channels': 'list[int]',
        'last_update_date': 'datetime',
        'record_formats': 'list[int]',
        'record_states': 'list[int]',
        'remove_deleted_telecasts': 'bool',
        'tags': 'list[str]',
        'exclude_repeated_broadcasts': 'bool',
        'tv_stations': 'list[int]',
        'excluded_tv_stations': 'list[int]',
        'tv_categories': 'list[int]',
        'tv_sub_categories': 'list[int]',
        'q': 'str',
        'is_highlight': 'bool',
        'max_end_date': 'datetime',
        'max_start_date': 'datetime',
        'min_end_date': 'datetime',
        'min_start_date': 'datetime',
        'max_start_time': 'str',
        'min_start_time': 'str',
        'day_of_weeks': 'list[int]',
        'search_text_scope': 'int',
        'star_ids': 'list[int]',
        'telecast_ids': 'list[int]',
        'time_block': 'int',
        'time_blocks': 'list[int]',
        'exact_title': 'str',
        'exact_titles': 'list[str]',
        'excluded_telecast_ids': 'list[int]',
        'fsk': 'list[int]'
    }

    attribute_map = {
        'ad_free_available': 'adFreeAvailable',
        'channels': 'channels',
        'last_update_date': 'lastUpdateDate',
        'record_formats': 'recordFormats',
        'record_states': 'recordStates',
        'remove_deleted_telecasts': 'removeDeletedTelecasts',
        'tags': 'tags',
        'exclude_repeated_broadcasts': 'excludeRepeatedBroadcasts',
        'tv_stations': 'tvStations',
        'excluded_tv_stations': 'excludedTvStations',
        'tv_categories': 'tvCategories',
        'tv_sub_categories': 'tvSubCategories',
        'q': 'q',
        'is_highlight': 'isHighlight',
        'max_end_date': 'maxEndDate',
        'max_start_date': 'maxStartDate',
        'min_end_date': 'minEndDate',
        'min_start_date': 'minStartDate',
        'max_start_time': 'maxStartTime',
        'min_start_time': 'minStartTime',
        'day_of_weeks': 'dayOfWeeks',
        'search_text_scope': 'searchTextScope',
        'star_ids': 'starIds',
        'telecast_ids': 'telecastIds',
        'time_block': 'timeBlock',
        'time_blocks': 'timeBlocks',
        'exact_title': 'exactTitle',
        'exact_titles': 'exactTitles',
        'excluded_telecast_ids': 'excludedTelecastIds',
        'fsk': 'fsk'
    }

    def __init__(self, ad_free_available=None, channels=None, last_update_date=None, record_formats=None, record_states=None, remove_deleted_telecasts=None, tags=None, exclude_repeated_broadcasts=None, tv_stations=None, excluded_tv_stations=None, tv_categories=None, tv_sub_categories=None, q=None, is_highlight=None, max_end_date=None, max_start_date=None, min_end_date=None, min_start_date=None, max_start_time=None, min_start_time=None, day_of_weeks=None, search_text_scope=None, star_ids=None, telecast_ids=None, time_block=None, time_blocks=None, exact_title=None, exact_titles=None, excluded_telecast_ids=None, fsk=None):  # noqa: E501
        """SaveTVWebApiRequestModelsRecordCountFilter - a model defined in Swagger"""  # noqa: E501

        self._ad_free_available = None
        self._channels = None
        self._last_update_date = None
        self._record_formats = None
        self._record_states = None
        self._remove_deleted_telecasts = None
        self._tags = None
        self._exclude_repeated_broadcasts = None
        self._tv_stations = None
        self._excluded_tv_stations = None
        self._tv_categories = None
        self._tv_sub_categories = None
        self._q = None
        self._is_highlight = None
        self._max_end_date = None
        self._max_start_date = None
        self._min_end_date = None
        self._min_start_date = None
        self._max_start_time = None
        self._min_start_time = None
        self._day_of_weeks = None
        self._search_text_scope = None
        self._star_ids = None
        self._telecast_ids = None
        self._time_block = None
        self._time_blocks = None
        self._exact_title = None
        self._exact_titles = None
        self._excluded_telecast_ids = None
        self._fsk = None
        self.discriminator = None

        if ad_free_available is not None:
            self.ad_free_available = ad_free_available
        if channels is not None:
            self.channels = channels
        if last_update_date is not None:
            self.last_update_date = last_update_date
        if record_formats is not None:
            self.record_formats = record_formats
        if record_states is not None:
            self.record_states = record_states
        if remove_deleted_telecasts is not None:
            self.remove_deleted_telecasts = remove_deleted_telecasts
        if tags is not None:
            self.tags = tags
        if exclude_repeated_broadcasts is not None:
            self.exclude_repeated_broadcasts = exclude_repeated_broadcasts
        if tv_stations is not None:
            self.tv_stations = tv_stations
        if excluded_tv_stations is not None:
            self.excluded_tv_stations = excluded_tv_stations
        if tv_categories is not None:
            self.tv_categories = tv_categories
        if tv_sub_categories is not None:
            self.tv_sub_categories = tv_sub_categories
        if q is not None:
            self.q = q
        if is_highlight is not None:
            self.is_highlight = is_highlight
        if max_end_date is not None:
            self.max_end_date = max_end_date
        if max_start_date is not None:
            self.max_start_date = max_start_date
        if min_end_date is not None:
            self.min_end_date = min_end_date
        if min_start_date is not None:
            self.min_start_date = min_start_date
        if max_start_time is not None:
            self.max_start_time = max_start_time
        if min_start_time is not None:
            self.min_start_time = min_start_time
        if day_of_weeks is not None:
            self.day_of_weeks = day_of_weeks
        if search_text_scope is not None:
            self.search_text_scope = search_text_scope
        if star_ids is not None:
            self.star_ids = star_ids
        if telecast_ids is not None:
            self.telecast_ids = telecast_ids
        if time_block is not None:
            self.time_block = time_block
        if time_blocks is not None:
            self.time_blocks = time_blocks
        if exact_title is not None:
            self.exact_title = exact_title
        if exact_titles is not None:
            self.exact_titles = exact_titles
        if excluded_telecast_ids is not None:
            self.excluded_telecast_ids = excluded_telecast_ids
        if fsk is not None:
            self.fsk = fsk

    @property
    def ad_free_available(self):
        """Gets the ad_free_available of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The ad_free_available of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: bool
        """
        return self._ad_free_available

    @ad_free_available.setter
    def ad_free_available(self, ad_free_available):
        """Sets the ad_free_available of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param ad_free_available: The ad_free_available of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: bool
        """

        self._ad_free_available = ad_free_available

    @property
    def channels(self):
        """Gets the channels of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The channels of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param channels: The channels of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._channels = channels

    @property
    def last_update_date(self):
        """Gets the last_update_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The last_update_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param last_update_date: The last_update_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: datetime
        """

        self._last_update_date = last_update_date

    @property
    def record_formats(self):
        """Gets the record_formats of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The record_formats of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._record_formats

    @record_formats.setter
    def record_formats(self, record_formats):
        """Sets the record_formats of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param record_formats: The record_formats of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """
        allowed_values = [4, 5, 6]  # noqa: E501
        if not set(record_formats).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `record_formats` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(record_formats) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._record_formats = record_formats

    @property
    def record_states(self):
        """Gets the record_states of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The record_states of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._record_states

    @record_states.setter
    def record_states(self, record_states):
        """Sets the record_states of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param record_states: The record_states of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """
        allowed_values = [1, 2, 3, 4, 5]  # noqa: E501
        if not set(record_states).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `record_states` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(record_states) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._record_states = record_states

    @property
    def remove_deleted_telecasts(self):
        """Gets the remove_deleted_telecasts of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The remove_deleted_telecasts of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: bool
        """
        return self._remove_deleted_telecasts

    @remove_deleted_telecasts.setter
    def remove_deleted_telecasts(self, remove_deleted_telecasts):
        """Sets the remove_deleted_telecasts of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param remove_deleted_telecasts: The remove_deleted_telecasts of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: bool
        """

        self._remove_deleted_telecasts = remove_deleted_telecasts

    @property
    def tags(self):
        """Gets the tags of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The tags of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param tags: The tags of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def exclude_repeated_broadcasts(self):
        """Gets the exclude_repeated_broadcasts of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The exclude_repeated_broadcasts of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_repeated_broadcasts

    @exclude_repeated_broadcasts.setter
    def exclude_repeated_broadcasts(self, exclude_repeated_broadcasts):
        """Sets the exclude_repeated_broadcasts of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param exclude_repeated_broadcasts: The exclude_repeated_broadcasts of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: bool
        """

        self._exclude_repeated_broadcasts = exclude_repeated_broadcasts

    @property
    def tv_stations(self):
        """Gets the tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._tv_stations

    @tv_stations.setter
    def tv_stations(self, tv_stations):
        """Sets the tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param tv_stations: The tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._tv_stations = tv_stations

    @property
    def excluded_tv_stations(self):
        """Gets the excluded_tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The excluded_tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_tv_stations

    @excluded_tv_stations.setter
    def excluded_tv_stations(self, excluded_tv_stations):
        """Sets the excluded_tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param excluded_tv_stations: The excluded_tv_stations of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._excluded_tv_stations = excluded_tv_stations

    @property
    def tv_categories(self):
        """Gets the tv_categories of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The tv_categories of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._tv_categories

    @tv_categories.setter
    def tv_categories(self, tv_categories):
        """Sets the tv_categories of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param tv_categories: The tv_categories of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._tv_categories = tv_categories

    @property
    def tv_sub_categories(self):
        """Gets the tv_sub_categories of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The tv_sub_categories of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._tv_sub_categories

    @tv_sub_categories.setter
    def tv_sub_categories(self, tv_sub_categories):
        """Sets the tv_sub_categories of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param tv_sub_categories: The tv_sub_categories of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._tv_sub_categories = tv_sub_categories

    @property
    def q(self):
        """Gets the q of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The q of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param q: The q of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: str
        """

        self._q = q

    @property
    def is_highlight(self):
        """Gets the is_highlight of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The is_highlight of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_highlight

    @is_highlight.setter
    def is_highlight(self, is_highlight):
        """Sets the is_highlight of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param is_highlight: The is_highlight of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: bool
        """

        self._is_highlight = is_highlight

    @property
    def max_end_date(self):
        """Gets the max_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The max_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._max_end_date

    @max_end_date.setter
    def max_end_date(self, max_end_date):
        """Sets the max_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param max_end_date: The max_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: datetime
        """

        self._max_end_date = max_end_date

    @property
    def max_start_date(self):
        """Gets the max_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The max_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._max_start_date

    @max_start_date.setter
    def max_start_date(self, max_start_date):
        """Sets the max_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param max_start_date: The max_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: datetime
        """

        self._max_start_date = max_start_date

    @property
    def min_end_date(self):
        """Gets the min_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The min_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._min_end_date

    @min_end_date.setter
    def min_end_date(self, min_end_date):
        """Sets the min_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param min_end_date: The min_end_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: datetime
        """

        self._min_end_date = min_end_date

    @property
    def min_start_date(self):
        """Gets the min_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The min_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._min_start_date

    @min_start_date.setter
    def min_start_date(self, min_start_date):
        """Sets the min_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param min_start_date: The min_start_date of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: datetime
        """

        self._min_start_date = min_start_date

    @property
    def max_start_time(self):
        """Gets the max_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The max_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: str
        """
        return self._max_start_time

    @max_start_time.setter
    def max_start_time(self, max_start_time):
        """Sets the max_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param max_start_time: The max_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: str
        """
        if max_start_time is not None and len(max_start_time) > 5:
            raise ValueError("Invalid value for `max_start_time`, length must be less than or equal to `5`")  # noqa: E501

        self._max_start_time = max_start_time

    @property
    def min_start_time(self):
        """Gets the min_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The min_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: str
        """
        return self._min_start_time

    @min_start_time.setter
    def min_start_time(self, min_start_time):
        """Sets the min_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param min_start_time: The min_start_time of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: str
        """
        if min_start_time is not None and len(min_start_time) > 5:
            raise ValueError("Invalid value for `min_start_time`, length must be less than or equal to `5`")  # noqa: E501

        self._min_start_time = min_start_time

    @property
    def day_of_weeks(self):
        """Gets the day_of_weeks of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The day_of_weeks of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._day_of_weeks

    @day_of_weeks.setter
    def day_of_weeks(self, day_of_weeks):
        """Sets the day_of_weeks of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param day_of_weeks: The day_of_weeks of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6]  # noqa: E501
        if not set(day_of_weeks).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `day_of_weeks` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(day_of_weeks) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._day_of_weeks = day_of_weeks

    @property
    def search_text_scope(self):
        """Gets the search_text_scope of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The search_text_scope of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: int
        """
        return self._search_text_scope

    @search_text_scope.setter
    def search_text_scope(self, search_text_scope):
        """Sets the search_text_scope of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param search_text_scope: The search_text_scope of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if search_text_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `search_text_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(search_text_scope, allowed_values)
            )

        self._search_text_scope = search_text_scope

    @property
    def star_ids(self):
        """Gets the star_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The star_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._star_ids

    @star_ids.setter
    def star_ids(self, star_ids):
        """Sets the star_ids of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param star_ids: The star_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._star_ids = star_ids

    @property
    def telecast_ids(self):
        """Gets the telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._telecast_ids

    @telecast_ids.setter
    def telecast_ids(self, telecast_ids):
        """Sets the telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param telecast_ids: The telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._telecast_ids = telecast_ids

    @property
    def time_block(self):
        """Gets the time_block of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The time_block of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: int
        """
        return self._time_block

    @time_block.setter
    def time_block(self, time_block):
        """Sets the time_block of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param time_block: The time_block of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # noqa: E501
        if time_block not in allowed_values:
            raise ValueError(
                "Invalid value for `time_block` ({0}), must be one of {1}"  # noqa: E501
                .format(time_block, allowed_values)
            )

        self._time_block = time_block

    @property
    def time_blocks(self):
        """Gets the time_blocks of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The time_blocks of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._time_blocks

    @time_blocks.setter
    def time_blocks(self, time_blocks):
        """Sets the time_blocks of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param time_blocks: The time_blocks of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """
        allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # noqa: E501
        if not set(time_blocks).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `time_blocks` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(time_blocks) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._time_blocks = time_blocks

    @property
    def exact_title(self):
        """Gets the exact_title of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The exact_title of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: str
        """
        return self._exact_title

    @exact_title.setter
    def exact_title(self, exact_title):
        """Sets the exact_title of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param exact_title: The exact_title of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: str
        """

        self._exact_title = exact_title

    @property
    def exact_titles(self):
        """Gets the exact_titles of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The exact_titles of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._exact_titles

    @exact_titles.setter
    def exact_titles(self, exact_titles):
        """Sets the exact_titles of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param exact_titles: The exact_titles of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[str]
        """

        self._exact_titles = exact_titles

    @property
    def excluded_telecast_ids(self):
        """Gets the excluded_telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The excluded_telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_telecast_ids

    @excluded_telecast_ids.setter
    def excluded_telecast_ids(self, excluded_telecast_ids):
        """Sets the excluded_telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param excluded_telecast_ids: The excluded_telecast_ids of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._excluded_telecast_ids = excluded_telecast_ids

    @property
    def fsk(self):
        """Gets the fsk of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501


        :return: The fsk of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._fsk

    @fsk.setter
    def fsk(self, fsk):
        """Sets the fsk of this SaveTVWebApiRequestModelsRecordCountFilter.


        :param fsk: The fsk of this SaveTVWebApiRequestModelsRecordCountFilter.  # noqa: E501
        :type: list[int]
        """

        self._fsk = fsk

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
        if issubclass(SaveTVWebApiRequestModelsRecordCountFilter, dict):
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
        if not isinstance(other, SaveTVWebApiRequestModelsRecordCountFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other