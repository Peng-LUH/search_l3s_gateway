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

class OrganizationJsonldOrganizationRead(object):
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
        'id': 'str',
        'type': 'str',
        'id': 'int',
        'name': 'str',
        'streetno': 'str',
        'zip': 'str',
        'city': 'str',
        'country': 'str',
        'settings': 'str',
        'task_sets': 'list[str]',
        'form_sets': 'list[str]',
        'groups': 'list[str]',
        'jobs': 'list[str]',
        'equipment': 'list[str]',
        'equipment_locations': 'list[str]',
        'app_tags': 'list[str]',
        'shared_task_sets': 'list[str]',
        'user_invitations': 'list[str]',
        'organization_in_group': 'str'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'name': 'name',
        'streetno': 'streetno',
        'zip': 'zip',
        'city': 'city',
        'country': 'country',
        'settings': 'settings',
        'task_sets': 'taskSets',
        'form_sets': 'formSets',
        'groups': 'groups',
        'jobs': 'jobs',
        'equipment': 'equipment',
        'equipment_locations': 'equipmentLocations',
        'app_tags': 'appTags',
        'shared_task_sets': 'sharedTaskSets',
        'user_invitations': 'userInvitations',
        'organization_in_group': 'organizationInGroup'
    }

    def __init__(self, id=None, type=None, id=None, name=None, streetno=None, zip=None, city=None, country=None, settings=None, task_sets=None, form_sets=None, groups=None, jobs=None, equipment=None, equipment_locations=None, app_tags=None, shared_task_sets=None, user_invitations=None, organization_in_group=None):  # noqa: E501
        """OrganizationJsonldOrganizationRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._id = None
        self._name = None
        self._streetno = None
        self._zip = None
        self._city = None
        self._country = None
        self._settings = None
        self._task_sets = None
        self._form_sets = None
        self._groups = None
        self._jobs = None
        self._equipment = None
        self._equipment_locations = None
        self._app_tags = None
        self._shared_task_sets = None
        self._user_invitations = None
        self._organization_in_group = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        self.name = name
        self.streetno = streetno
        self.zip = zip
        self.city = city
        self.country = country
        if settings is not None:
            self.settings = settings
        if task_sets is not None:
            self.task_sets = task_sets
        if form_sets is not None:
            self.form_sets = form_sets
        if groups is not None:
            self.groups = groups
        if jobs is not None:
            self.jobs = jobs
        if equipment is not None:
            self.equipment = equipment
        if equipment_locations is not None:
            self.equipment_locations = equipment_locations
        if app_tags is not None:
            self.app_tags = app_tags
        if shared_task_sets is not None:
            self.shared_task_sets = shared_task_sets
        if user_invitations is not None:
            self.user_invitations = user_invitations
        if organization_in_group is not None:
            self.organization_in_group = organization_in_group

    @property
    def id(self):
        """Gets the id of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The id of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationJsonldOrganizationRead.


        :param id: The id of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The type of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrganizationJsonldOrganizationRead.


        :param type: The type of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The id of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationJsonldOrganizationRead.


        :param id: The id of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The name of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationJsonldOrganizationRead.


        :param name: The name of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def streetno(self):
        """Gets the streetno of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The streetno of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._streetno

    @streetno.setter
    def streetno(self, streetno):
        """Sets the streetno of this OrganizationJsonldOrganizationRead.


        :param streetno: The streetno of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """
        if streetno is None:
            raise ValueError("Invalid value for `streetno`, must not be `None`")  # noqa: E501

        self._streetno = streetno

    @property
    def zip(self):
        """Gets the zip of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The zip of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this OrganizationJsonldOrganizationRead.


        :param zip: The zip of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def city(self):
        """Gets the city of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The city of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrganizationJsonldOrganizationRead.


        :param city: The city of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def country(self):
        """Gets the country of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The country of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OrganizationJsonldOrganizationRead.


        :param country: The country of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def settings(self):
        """Gets the settings of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The settings of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this OrganizationJsonldOrganizationRead.


        :param settings: The settings of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """

        self._settings = settings

    @property
    def task_sets(self):
        """Gets the task_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The task_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_sets

    @task_sets.setter
    def task_sets(self, task_sets):
        """Sets the task_sets of this OrganizationJsonldOrganizationRead.


        :param task_sets: The task_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._task_sets = task_sets

    @property
    def form_sets(self):
        """Gets the form_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The form_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_sets

    @form_sets.setter
    def form_sets(self, form_sets):
        """Sets the form_sets of this OrganizationJsonldOrganizationRead.


        :param form_sets: The form_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._form_sets = form_sets

    @property
    def groups(self):
        """Gets the groups of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The groups of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this OrganizationJsonldOrganizationRead.


        :param groups: The groups of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def jobs(self):
        """Gets the jobs of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The jobs of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this OrganizationJsonldOrganizationRead.


        :param jobs: The jobs of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._jobs = jobs

    @property
    def equipment(self):
        """Gets the equipment of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The equipment of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this OrganizationJsonldOrganizationRead.


        :param equipment: The equipment of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._equipment = equipment

    @property
    def equipment_locations(self):
        """Gets the equipment_locations of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The equipment_locations of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment_locations

    @equipment_locations.setter
    def equipment_locations(self, equipment_locations):
        """Sets the equipment_locations of this OrganizationJsonldOrganizationRead.


        :param equipment_locations: The equipment_locations of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._equipment_locations = equipment_locations

    @property
    def app_tags(self):
        """Gets the app_tags of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The app_tags of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_tags

    @app_tags.setter
    def app_tags(self, app_tags):
        """Sets the app_tags of this OrganizationJsonldOrganizationRead.


        :param app_tags: The app_tags of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._app_tags = app_tags

    @property
    def shared_task_sets(self):
        """Gets the shared_task_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The shared_task_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_task_sets

    @shared_task_sets.setter
    def shared_task_sets(self, shared_task_sets):
        """Sets the shared_task_sets of this OrganizationJsonldOrganizationRead.


        :param shared_task_sets: The shared_task_sets of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_task_sets = shared_task_sets

    @property
    def user_invitations(self):
        """Gets the user_invitations of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The user_invitations of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_invitations

    @user_invitations.setter
    def user_invitations(self, user_invitations):
        """Sets the user_invitations of this OrganizationJsonldOrganizationRead.


        :param user_invitations: The user_invitations of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: list[str]
        """

        self._user_invitations = user_invitations

    @property
    def organization_in_group(self):
        """Gets the organization_in_group of this OrganizationJsonldOrganizationRead.  # noqa: E501


        :return: The organization_in_group of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._organization_in_group

    @organization_in_group.setter
    def organization_in_group(self, organization_in_group):
        """Sets the organization_in_group of this OrganizationJsonldOrganizationRead.


        :param organization_in_group: The organization_in_group of this OrganizationJsonldOrganizationRead.  # noqa: E501
        :type: str
        """

        self._organization_in_group = organization_in_group

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
        if issubclass(OrganizationJsonldOrganizationRead, dict):
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
        if not isinstance(other, OrganizationJsonldOrganizationRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other