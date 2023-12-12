# coding: utf-8

"""
    MLS2 API

    Central API  # noqa: E501

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserCommentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_user_comment_collection(self, **kwargs):  # noqa: E501
        """Retrieves the collection of UserComment resources.  # noqa: E501

        Retrieves the collection of UserComment resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_comment_collection(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The collection page number
        :param int items_per_page: The number of items per page
        :param bool pagination: Enable or disable pagination
        :param str user:
        :param list[str] user:
        :param str organization:
        :param list[str] organization:
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_comment_collection_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_comment_collection_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_comment_collection_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves the collection of UserComment resources.  # noqa: E501

        Retrieves the collection of UserComment resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_comment_collection_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The collection page number
        :param int items_per_page: The number of items per page
        :param bool pagination: Enable or disable pagination
        :param str user:
        :param list[str] user:
        :param str organization:
        :param list[str] organization:
        :return: InlineResponse20078
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'items_per_page', 'pagination', 'user', 'user', 'organization', 'organization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_comment_collection" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'items_per_page' in params:
            query_params.append(('itemsPerPage', params['items_per_page']))  # noqa: E501
        if 'pagination' in params:
            query_params.append(('pagination', params['pagination']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user[]', params['user']))  # noqa: E501
            collection_formats['user[]'] = 'multi'  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization[]', params['organization']))  # noqa: E501
            collection_formats['organization[]'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/user-comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20078',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_comment_item(self, id, **kwargs):  # noqa: E501
        """Retrieves a UserComment resource.  # noqa: E501

        Retrieves a UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_comment_item(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Resource identifier (required)
        :return: UserCommentJsonldUserCommentItemRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_comment_item_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_comment_item_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_user_comment_item_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a UserComment resource.  # noqa: E501

        Retrieves a UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_comment_item_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Resource identifier (required)
        :return: UserCommentJsonldUserCommentItemRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_comment_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_user_comment_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/user-comments/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserCommentJsonldUserCommentItemRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_user_comment_collection(self, body, **kwargs):  # noqa: E501
        """Creates a UserComment resource.  # noqa: E501

        Creates a UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_comment_collection(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentWrite body: The new UserComment resource (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_user_comment_collection_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_user_comment_collection_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_user_comment_collection_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a UserComment resource.  # noqa: E501

        Creates a UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_comment_collection_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentWrite body: The new UserComment resource (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_user_comment_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_user_comment_collection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/user-comments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserCommentJsonld',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_user_comment_collection(self, body, **kwargs):  # noqa: E501
        """Creates a UserComment resource.  # noqa: E501

        Creates a UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_comment_collection(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentWrite body: The new UserComment resource (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_user_comment_collection_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_user_comment_collection_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_user_comment_collection_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a UserComment resource.  # noqa: E501

        Creates a UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_comment_collection_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentWrite body: The new UserComment resource (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_user_comment_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_user_comment_collection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/user-comments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserCommentJsonld',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_user_comment_item(self, body, id, **kwargs):  # noqa: E501
        """Replaces the UserComment resource.  # noqa: E501

        Replaces the UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_user_comment_item(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentItemWrite body: The updated UserComment resource (required)
        :param str id: Resource identifier (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_user_comment_item_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_user_comment_item_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def put_user_comment_item_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Replaces the UserComment resource.  # noqa: E501

        Replaces the UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_user_comment_item_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentItemWrite body: The updated UserComment resource (required)
        :param str id: Resource identifier (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_user_comment_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_user_comment_item`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `put_user_comment_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/user-comments/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserCommentJsonld',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_user_comment_item(self, body, id, **kwargs):  # noqa: E501
        """Replaces the UserComment resource.  # noqa: E501

        Replaces the UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_user_comment_item(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentItemWrite body: The updated UserComment resource (required)
        :param str id: Resource identifier (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_user_comment_item_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_user_comment_item_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def put_user_comment_item_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Replaces the UserComment resource.  # noqa: E501

        Replaces the UserComment resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_user_comment_item_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserCommentJsonldUserCommentItemWrite body: The updated UserComment resource (required)
        :param str id: Resource identifier (required)
        :return: UserCommentJsonld
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_user_comment_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_user_comment_item`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `put_user_comment_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/user-comments/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserCommentJsonld',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)