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


class SaveTVEpgDataContextChannel(object):
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
        'user_id': 'int',
        'create_date': 'datetime',
        'delete_date': 'datetime',
        'name': 'str',
        'record_process_date': 'datetime'
    }

    attribute_map = {
        'id': 'Id',
        'user_id': 'UserId',
        'create_date': 'CreateDate',
        'delete_date': 'DeleteDate',
        'name': 'Name',
        'record_process_date': 'RecordProcessDate'
    }

    def __init__(self, id=None, user_id=None, create_date=None, delete_date=None, name=None, record_process_date=None):  # noqa: E501
        """SaveTVEpgDataContextChannel - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user_id = None
        self._create_date = None
        self._delete_date = None
        self._name = None
        self._record_process_date = None
        self.discriminator = None

        self.id = id
        self.user_id = user_id
        self.create_date = create_date
        if delete_date is not None:
            self.delete_date = delete_date
        self.name = name
        if record_process_date is not None:
            self.record_process_date = record_process_date

    @property
    def id(self):
        """Gets the id of this SaveTVEpgDataContextChannel.  # noqa: E501


        :return: The id of this SaveTVEpgDataContextChannel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaveTVEpgDataContextChannel.


        :param id: The id of this SaveTVEpgDataContextChannel.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this SaveTVEpgDataContextChannel.  # noqa: E501


        :return: The user_id of this SaveTVEpgDataContextChannel.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SaveTVEpgDataContextChannel.


        :param user_id: The user_id of this SaveTVEpgDataContextChannel.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def create_date(self):
        """Gets the create_date of this SaveTVEpgDataContextChannel.  # noqa: E501


        :return: The create_date of this SaveTVEpgDataContextChannel.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this SaveTVEpgDataContextChannel.


        :param create_date: The create_date of this SaveTVEpgDataContextChannel.  # noqa: E501
        :type: datetime
        """
        if create_date is None:
            raise ValueError("Invalid value for `create_date`, must not be `None`")  # noqa: E501

        self._create_date = create_date

    @property
    def delete_date(self):
        """Gets the delete_date of this SaveTVEpgDataContextChannel.  # noqa: E501


        :return: The delete_date of this SaveTVEpgDataContextChannel.  # noqa: E501
        :rtype: datetime
        """
        return self._delete_date

    @delete_date.setter
    def delete_date(self, delete_date):
        """Sets the delete_date of this SaveTVEpgDataContextChannel.


        :param delete_date: The delete_date of this SaveTVEpgDataContextChannel.  # noqa: E501
        :type: datetime
        """

        self._delete_date = delete_date

    @property
    def name(self):
        """Gets the name of this SaveTVEpgDataContextChannel.  # noqa: E501


        :return: The name of this SaveTVEpgDataContextChannel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTVEpgDataContextChannel.


        :param name: The name of this SaveTVEpgDataContextChannel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def record_process_date(self):
        """Gets the record_process_date of this SaveTVEpgDataContextChannel.  # noqa: E501


        :return: The record_process_date of this SaveTVEpgDataContextChannel.  # noqa: E501
        :rtype: datetime
        """
        return self._record_process_date

    @record_process_date.setter
    def record_process_date(self, record_process_date):
        """Sets the record_process_date of this SaveTVEpgDataContextChannel.


        :param record_process_date: The record_process_date of this SaveTVEpgDataContextChannel.  # noqa: E501
        :type: datetime
        """

        self._record_process_date = record_process_date

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
        if issubclass(SaveTVEpgDataContextChannel, dict):
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
        if not isinstance(other, SaveTVEpgDataContextChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
