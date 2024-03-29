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

class PrivacyJsonldPrivacyWrite(object):
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
        'context': 'OneOfPrivacyJsonldPrivacyWriteContext',
        'id': 'str',
        'type': 'str',
        'id': 'int',
        'excerpt': 'str',
        'text': 'str',
        'active': 'bool',
        'version': 'str',
        'organization': 'str',
        'privacy_pdf': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'excerpt': 'excerpt',
        'text': 'text',
        'active': 'active',
        'version': 'version',
        'organization': 'organization',
        'privacy_pdf': 'privacyPDF'
    }

    def __init__(self, context=None, id=None, type=None, id=None, excerpt=None, text=None, active=None, version=None, organization=None, privacy_pdf=None):  # noqa: E501
        """PrivacyJsonldPrivacyWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._id = None
        self._excerpt = None
        self._text = None
        self._active = None
        self._version = None
        self._organization = None
        self._privacy_pdf = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if excerpt is not None:
            self.excerpt = excerpt
        if text is not None:
            self.text = text
        if active is not None:
            self.active = active
        if version is not None:
            self.version = version
        if organization is not None:
            self.organization = organization
        if privacy_pdf is not None:
            self.privacy_pdf = privacy_pdf

    @property
    def context(self):
        """Gets the context of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The context of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: OneOfPrivacyJsonldPrivacyWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PrivacyJsonldPrivacyWrite.


        :param context: The context of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: OneOfPrivacyJsonldPrivacyWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The id of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivacyJsonldPrivacyWrite.


        :param id: The id of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The type of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PrivacyJsonldPrivacyWrite.


        :param type: The type of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The id of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivacyJsonldPrivacyWrite.


        :param id: The id of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def excerpt(self):
        """Gets the excerpt of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The excerpt of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: str
        """
        return self._excerpt

    @excerpt.setter
    def excerpt(self, excerpt):
        """Sets the excerpt of this PrivacyJsonldPrivacyWrite.


        :param excerpt: The excerpt of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: str
        """

        self._excerpt = excerpt

    @property
    def text(self):
        """Gets the text of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The text of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PrivacyJsonldPrivacyWrite.


        :param text: The text of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def active(self):
        """Gets the active of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The active of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PrivacyJsonldPrivacyWrite.


        :param active: The active of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def version(self):
        """Gets the version of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The version of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PrivacyJsonldPrivacyWrite.


        :param version: The version of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def organization(self):
        """Gets the organization of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The organization of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this PrivacyJsonldPrivacyWrite.


        :param organization: The organization of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def privacy_pdf(self):
        """Gets the privacy_pdf of this PrivacyJsonldPrivacyWrite.  # noqa: E501


        :return: The privacy_pdf of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :rtype: str
        """
        return self._privacy_pdf

    @privacy_pdf.setter
    def privacy_pdf(self, privacy_pdf):
        """Sets the privacy_pdf of this PrivacyJsonldPrivacyWrite.


        :param privacy_pdf: The privacy_pdf of this PrivacyJsonldPrivacyWrite.  # noqa: E501
        :type: str
        """

        self._privacy_pdf = privacy_pdf

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
        if issubclass(PrivacyJsonldPrivacyWrite, dict):
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
        if not isinstance(other, PrivacyJsonldPrivacyWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
