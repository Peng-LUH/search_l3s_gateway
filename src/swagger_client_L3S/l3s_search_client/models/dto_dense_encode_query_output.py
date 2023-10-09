# coding: utf-8

"""
    L3S Search Service for SEARCH

    Welcome to the Swagger UI documentation site test!  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoDenseEncodeQueryOutput(object):
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
        'dense_encode': 'list[float]'
    }

    attribute_map = {
        'dense_encode': 'dense_encode'
    }

    def __init__(self, dense_encode=None):  # noqa: E501
        """DtoDenseEncodeQueryOutput - a model defined in Swagger"""  # noqa: E501
        self._dense_encode = None
        self.discriminator = None
        if dense_encode is not None:
            self.dense_encode = dense_encode

    @property
    def dense_encode(self):
        """Gets the dense_encode of this DtoDenseEncodeQueryOutput.  # noqa: E501


        :return: The dense_encode of this DtoDenseEncodeQueryOutput.  # noqa: E501
        :rtype: list[float]
        """
        return self._dense_encode

    @dense_encode.setter
    def dense_encode(self, dense_encode):
        """Sets the dense_encode of this DtoDenseEncodeQueryOutput.


        :param dense_encode: The dense_encode of this DtoDenseEncodeQueryOutput.  # noqa: E501
        :type: list[float]
        """

        self._dense_encode = dense_encode

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
        if issubclass(DtoDenseEncodeQueryOutput, dict):
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
        if not isinstance(other, DtoDenseEncodeQueryOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other