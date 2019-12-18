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


class SaveTVWebApiResponseModelsPlaylistType(object):
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
        'is_owned_by_account': 'bool',
        'name_can_be_changed': 'bool',
        'is_public_can_be_changed': 'bool',
        'can_be_deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_owned_by_account': 'isOwnedByAccount',
        'name_can_be_changed': 'nameCanBeChanged',
        'is_public_can_be_changed': 'isPublicCanBeChanged',
        'can_be_deleted': 'canBeDeleted'
    }

    def __init__(self, id=None, name=None, is_owned_by_account=None, name_can_be_changed=None, is_public_can_be_changed=None, can_be_deleted=None):  # noqa: E501
        """SaveTVWebApiResponseModelsPlaylistType - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._is_owned_by_account = None
        self._name_can_be_changed = None
        self._is_public_can_be_changed = None
        self._can_be_deleted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_owned_by_account is not None:
            self.is_owned_by_account = is_owned_by_account
        if name_can_be_changed is not None:
            self.name_can_be_changed = name_can_be_changed
        if is_public_can_be_changed is not None:
            self.is_public_can_be_changed = is_public_can_be_changed
        if can_be_deleted is not None:
            self.can_be_deleted = can_be_deleted

    @property
    def id(self):
        """Gets the id of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501


        :return: The id of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaveTVWebApiResponseModelsPlaylistType.


        :param id: The id of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501


        :return: The name of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveTVWebApiResponseModelsPlaylistType.


        :param name: The name of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_owned_by_account(self):
        """Gets the is_owned_by_account of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501


        :return: The is_owned_by_account of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :rtype: bool
        """
        return self._is_owned_by_account

    @is_owned_by_account.setter
    def is_owned_by_account(self, is_owned_by_account):
        """Sets the is_owned_by_account of this SaveTVWebApiResponseModelsPlaylistType.


        :param is_owned_by_account: The is_owned_by_account of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :type: bool
        """

        self._is_owned_by_account = is_owned_by_account

    @property
    def name_can_be_changed(self):
        """Gets the name_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501


        :return: The name_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :rtype: bool
        """
        return self._name_can_be_changed

    @name_can_be_changed.setter
    def name_can_be_changed(self, name_can_be_changed):
        """Sets the name_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.


        :param name_can_be_changed: The name_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :type: bool
        """

        self._name_can_be_changed = name_can_be_changed

    @property
    def is_public_can_be_changed(self):
        """Gets the is_public_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501


        :return: The is_public_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :rtype: bool
        """
        return self._is_public_can_be_changed

    @is_public_can_be_changed.setter
    def is_public_can_be_changed(self, is_public_can_be_changed):
        """Sets the is_public_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.


        :param is_public_can_be_changed: The is_public_can_be_changed of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :type: bool
        """

        self._is_public_can_be_changed = is_public_can_be_changed

    @property
    def can_be_deleted(self):
        """Gets the can_be_deleted of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501


        :return: The can_be_deleted of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_deleted

    @can_be_deleted.setter
    def can_be_deleted(self, can_be_deleted):
        """Sets the can_be_deleted of this SaveTVWebApiResponseModelsPlaylistType.


        :param can_be_deleted: The can_be_deleted of this SaveTVWebApiResponseModelsPlaylistType.  # noqa: E501
        :type: bool
        """

        self._can_be_deleted = can_be_deleted

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
        if issubclass(SaveTVWebApiResponseModelsPlaylistType, dict):
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
        if not isinstance(other, SaveTVWebApiResponseModelsPlaylistType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other