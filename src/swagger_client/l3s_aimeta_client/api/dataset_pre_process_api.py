# coding: utf-8

"""
    L3S AI-Meta Service(AIMS) for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 0.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from l3s_aimeta_client.api_client import ApiClient


class DatasetPreProcessApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_get_task_steps(self, task_id, **kwargs):  # noqa: E501
        """Retrieve a Preprocessed TaskStep Resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_task_steps(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: (required)
        :return: DtoTaskPreprocessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_get_task_steps_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_get_task_steps_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def get_get_task_steps_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Retrieve a Preprocessed TaskStep Resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_task_steps_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: (required)
        :return: DtoTaskPreprocessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_task_steps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `get_get_task_steps`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task_id'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/aims/preprocess-tasks/{task_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoTaskPreprocessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_get_task_steps_0(self, taskstep_id, **kwargs):  # noqa: E501
        """Retrieve a Preprocessed TaskStep Resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_task_steps_0(taskstep_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str taskstep_id: (required)
        :return: DtoTaskStepPreprocessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_get_task_steps_0_with_http_info(taskstep_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_get_task_steps_0_with_http_info(taskstep_id, **kwargs)  # noqa: E501
            return data

    def get_get_task_steps_0_with_http_info(self, taskstep_id, **kwargs):  # noqa: E501
        """Retrieve a Preprocessed TaskStep Resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_task_steps_0_with_http_info(taskstep_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str taskstep_id: (required)
        :return: DtoTaskStepPreprocessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['taskstep_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_task_steps_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'taskstep_id' is set
        if ('taskstep_id' not in params or
                params['taskstep_id'] is None):
            raise ValueError("Missing the required parameter `taskstep_id` when calling `get_get_task_steps_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'taskstep_id' in params:
            path_params['taskstep_id'] = params['taskstep_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/aims/preprocess-tasksteps/{taskstep_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoTaskStepPreprocessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
