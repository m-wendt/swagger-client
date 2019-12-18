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


class SaveTVWebApiRequestModelsStarNotificationDeleteRequest(object):
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
        'mail_cancellation_reason_id': 'int'
    }

    attribute_map = {
        'mail_cancellation_reason_id': 'mailCancellationReasonId'
    }

    def __init__(self, mail_cancellation_reason_id=None):  # noqa: E501
        """SaveTVWebApiRequestModelsStarNotificationDeleteRequest - a model defined in Swagger"""  # noqa: E501

        self._mail_cancellation_reason_id = None
        self.discriminator = None

        if mail_cancellation_reason_id is not None:
            self.mail_cancellation_reason_id = mail_cancellation_reason_id

    @property
    def mail_cancellation_reason_id(self):
        """Gets the mail_cancellation_reason_id of this SaveTVWebApiRequestModelsStarNotificationDeleteRequest.  # noqa: E501


        :return: The mail_cancellation_reason_id of this SaveTVWebApiRequestModelsStarNotificationDeleteRequest.  # noqa: E501
        :rtype: int
        """
        return self._mail_cancellation_reason_id

    @mail_cancellation_reason_id.setter
    def mail_cancellation_reason_id(self, mail_cancellation_reason_id):
        """Sets the mail_cancellation_reason_id of this SaveTVWebApiRequestModelsStarNotificationDeleteRequest.


        :param mail_cancellation_reason_id: The mail_cancellation_reason_id of this SaveTVWebApiRequestModelsStarNotificationDeleteRequest.  # noqa: E501
        :type: int
        """

        self._mail_cancellation_reason_id = mail_cancellation_reason_id

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
        if issubclass(SaveTVWebApiRequestModelsStarNotificationDeleteRequest, dict):
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
        if not isinstance(other, SaveTVWebApiRequestModelsStarNotificationDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
