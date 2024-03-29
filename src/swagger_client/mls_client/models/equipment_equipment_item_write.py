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

class EquipmentEquipmentItemWrite(object):
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
        'name': 'str',
        'serial': 'str',
        'creator': 'str',
        'organization': 'str',
        'manufacturer': 'str',
        'category': 'str',
        'image': 'str',
        'location': 'str',
        'specification_category': 'list[str]',
        'files': 'list[str]',
        'file_links': 'list[str]',
        'task_todos': 'list[str]',
        'group_task_todos': 'list[str]',
        'equipment_maintenances': 'list[EquipmentMaintenanceEquipmentItemWrite]'
    }

    attribute_map = {
        'name': 'name',
        'serial': 'serial',
        'creator': 'creator',
        'organization': 'organization',
        'manufacturer': 'manufacturer',
        'category': 'category',
        'image': 'image',
        'location': 'location',
        'specification_category': 'specificationCategory',
        'files': 'files',
        'file_links': 'fileLinks',
        'task_todos': 'taskTodos',
        'group_task_todos': 'groupTaskTodos',
        'equipment_maintenances': 'equipmentMaintenances'
    }

    def __init__(self, name=None, serial=None, creator=None, organization=None, manufacturer=None, category=None, image=None, location=None, specification_category=None, files=None, file_links=None, task_todos=None, group_task_todos=None, equipment_maintenances=None):  # noqa: E501
        """EquipmentEquipmentItemWrite - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._serial = None
        self._creator = None
        self._organization = None
        self._manufacturer = None
        self._category = None
        self._image = None
        self._location = None
        self._specification_category = None
        self._files = None
        self._file_links = None
        self._task_todos = None
        self._group_task_todos = None
        self._equipment_maintenances = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if serial is not None:
            self.serial = serial
        if creator is not None:
            self.creator = creator
        if organization is not None:
            self.organization = organization
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if category is not None:
            self.category = category
        if image is not None:
            self.image = image
        if location is not None:
            self.location = location
        if specification_category is not None:
            self.specification_category = specification_category
        if files is not None:
            self.files = files
        if file_links is not None:
            self.file_links = file_links
        if task_todos is not None:
            self.task_todos = task_todos
        if group_task_todos is not None:
            self.group_task_todos = group_task_todos
        if equipment_maintenances is not None:
            self.equipment_maintenances = equipment_maintenances

    @property
    def name(self):
        """Gets the name of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The name of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EquipmentEquipmentItemWrite.


        :param name: The name of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def serial(self):
        """Gets the serial of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The serial of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this EquipmentEquipmentItemWrite.


        :param serial: The serial of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def creator(self):
        """Gets the creator of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The creator of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this EquipmentEquipmentItemWrite.


        :param creator: The creator of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def organization(self):
        """Gets the organization of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The organization of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this EquipmentEquipmentItemWrite.


        :param organization: The organization of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def manufacturer(self):
        """Gets the manufacturer of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The manufacturer of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this EquipmentEquipmentItemWrite.


        :param manufacturer: The manufacturer of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def category(self):
        """Gets the category of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The category of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EquipmentEquipmentItemWrite.


        :param category: The category of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def image(self):
        """Gets the image of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The image of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this EquipmentEquipmentItemWrite.


        :param image: The image of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def location(self):
        """Gets the location of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The location of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EquipmentEquipmentItemWrite.


        :param location: The location of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def specification_category(self):
        """Gets the specification_category of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The specification_category of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._specification_category

    @specification_category.setter
    def specification_category(self, specification_category):
        """Sets the specification_category of this EquipmentEquipmentItemWrite.


        :param specification_category: The specification_category of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._specification_category = specification_category

    @property
    def files(self):
        """Gets the files of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The files of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this EquipmentEquipmentItemWrite.


        :param files: The files of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._files = files

    @property
    def file_links(self):
        """Gets the file_links of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The file_links of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_links

    @file_links.setter
    def file_links(self, file_links):
        """Sets the file_links of this EquipmentEquipmentItemWrite.


        :param file_links: The file_links of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._file_links = file_links

    @property
    def task_todos(self):
        """Gets the task_todos of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The task_todos of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_todos

    @task_todos.setter
    def task_todos(self, task_todos):
        """Sets the task_todos of this EquipmentEquipmentItemWrite.


        :param task_todos: The task_todos of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._task_todos = task_todos

    @property
    def group_task_todos(self):
        """Gets the group_task_todos of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The group_task_todos of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_task_todos

    @group_task_todos.setter
    def group_task_todos(self, group_task_todos):
        """Sets the group_task_todos of this EquipmentEquipmentItemWrite.


        :param group_task_todos: The group_task_todos of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._group_task_todos = group_task_todos

    @property
    def equipment_maintenances(self):
        """Gets the equipment_maintenances of this EquipmentEquipmentItemWrite.  # noqa: E501


        :return: The equipment_maintenances of this EquipmentEquipmentItemWrite.  # noqa: E501
        :rtype: list[EquipmentMaintenanceEquipmentItemWrite]
        """
        return self._equipment_maintenances

    @equipment_maintenances.setter
    def equipment_maintenances(self, equipment_maintenances):
        """Sets the equipment_maintenances of this EquipmentEquipmentItemWrite.


        :param equipment_maintenances: The equipment_maintenances of this EquipmentEquipmentItemWrite.  # noqa: E501
        :type: list[EquipmentMaintenanceEquipmentItemWrite]
        """

        self._equipment_maintenances = equipment_maintenances

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
        if issubclass(EquipmentEquipmentItemWrite, dict):
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
        if not isinstance(other, EquipmentEquipmentItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
