# coding: utf-8

"""
    MLS2 API

    Central API  # noqa: E501

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20027(object):
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
        'hydramember': 'list[ExternalIliasCoursesJsonldExternalIliasCoursesRead]',
        'hydratotal_items': 'int',
        'hydraview': 'InlineResponse200Hydraview',
        'hydrasearch': 'InlineResponse200Hydrasearch'
    }

    attribute_map = {
        'hydramember': 'hydra:member',
        'hydratotal_items': 'hydra:totalItems',
        'hydraview': 'hydra:view',
        'hydrasearch': 'hydra:search'
    }

    def __init__(self, hydramember=None, hydratotal_items=None, hydraview=None, hydrasearch=None):  # noqa: E501
        """InlineResponse20027 - a model defined in Swagger"""  # noqa: E501
        self._hydramember = None
        self._hydratotal_items = None
        self._hydraview = None
        self._hydrasearch = None
        self.discriminator = None
        self.hydramember = hydramember
        if hydratotal_items is not None:
            self.hydratotal_items = hydratotal_items
        if hydraview is not None:
            self.hydraview = hydraview
        if hydrasearch is not None:
            self.hydrasearch = hydrasearch

    @property
    def hydramember(self):
        """Gets the hydramember of this InlineResponse20027.  # noqa: E501


        :return: The hydramember of this InlineResponse20027.  # noqa: E501
        :rtype: list[ExternalIliasCoursesJsonldExternalIliasCoursesRead]
        """
        return self._hydramember

    @hydramember.setter
    def hydramember(self, hydramember):
        """Sets the hydramember of this InlineResponse20027.


        :param hydramember: The hydramember of this InlineResponse20027.  # noqa: E501
        :type: list[ExternalIliasCoursesJsonldExternalIliasCoursesRead]
        """
        if hydramember is None:
            raise ValueError("Invalid value for `hydramember`, must not be `None`")  # noqa: E501

        self._hydramember = hydramember

    @property
    def hydratotal_items(self):
        """Gets the hydratotal_items of this InlineResponse20027.  # noqa: E501


        :return: The hydratotal_items of this InlineResponse20027.  # noqa: E501
        :rtype: int
        """
        return self._hydratotal_items

    @hydratotal_items.setter
    def hydratotal_items(self, hydratotal_items):
        """Sets the hydratotal_items of this InlineResponse20027.


        :param hydratotal_items: The hydratotal_items of this InlineResponse20027.  # noqa: E501
        :type: int
        """

        self._hydratotal_items = hydratotal_items

    @property
    def hydraview(self):
        """Gets the hydraview of this InlineResponse20027.  # noqa: E501


        :return: The hydraview of this InlineResponse20027.  # noqa: E501
        :rtype: InlineResponse200Hydraview
        """
        return self._hydraview

    @hydraview.setter
    def hydraview(self, hydraview):
        """Sets the hydraview of this InlineResponse20027.


        :param hydraview: The hydraview of this InlineResponse20027.  # noqa: E501
        :type: InlineResponse200Hydraview
        """

        self._hydraview = hydraview

    @property
    def hydrasearch(self):
        """Gets the hydrasearch of this InlineResponse20027.  # noqa: E501


        :return: The hydrasearch of this InlineResponse20027.  # noqa: E501
        :rtype: InlineResponse200Hydrasearch
        """
        return self._hydrasearch

    @hydrasearch.setter
    def hydrasearch(self, hydrasearch):
        """Sets the hydrasearch of this InlineResponse20027.


        :param hydrasearch: The hydrasearch of this InlineResponse20027.  # noqa: E501
        :type: InlineResponse200Hydrasearch
        """

        self._hydrasearch = hydrasearch

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
        if issubclass(InlineResponse20027, dict):
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
        if not isinstance(other, InlineResponse20027):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
