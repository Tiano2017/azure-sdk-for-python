# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
import uuid

from .. import models


class ServicePrincipalsOperations(object):
    """ServicePrincipalsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: Client Api Version. Constant value: "1.6".
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "1.6"

        self.config = config

    def create(
            self, parameters, custom_headers=None, raw=False, **operation_config):
        """Creates a service principal in the  directory.

        :param parameters: Parameters to create a service principal.
        :type parameters: :class:`ServicePrincipalCreateParameters
         <azure.graphrbac.models.ServicePrincipalCreateParameters>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`ServicePrincipal
         <azure.graphrbac.models.ServicePrincipal>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/{tenantID}/servicePrincipals'
        path_format_arguments = {
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ServicePrincipalCreateParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [201]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('ServicePrincipal', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def list(
            self, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets list of service principals from the current tenant.

        :param filter: The filter to apply on the operation.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`ServicePrincipalPaged
         <azure.graphrbac.models.ServicePrincipalPaged>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/{tenantID}/servicePrincipals'
                path_format_arguments = {
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = '/{tenantID}/{nextLink}'
                path_format_arguments = {
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ServicePrincipalPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ServicePrincipalPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def delete(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Deletes service principal from the directory.

        :param object_id: Object id to delete service principal information.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/{tenantID}/servicePrincipals/{objectId}'
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Gets service principal information from the directory.

        :param object_id: Object id to get service principal information.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`ServicePrincipal
         <azure.graphrbac.models.ServicePrincipal>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        # Construct URL
        url = '/{tenantID}/servicePrincipals/{objectId}'
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ServicePrincipal', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def list_key_credentials(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Get keyCredentials associated with the service principal by object Id.
        Reference:
        https://msdn.microsoft.com/en-us/library/azure/ad/graph/api/entity-and-complex-type-reference#keycredential-type.

        :param object_id: Object id to get service principal information.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`KeyCredentialPaged
         <azure.graphrbac.models.KeyCredentialPaged>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/{tenantID}/servicePrincipals/{objectId}/keyCredentials'
                path_format_arguments = {
                    'objectId': self._serialize.url("object_id", object_id, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.KeyCredentialPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.KeyCredentialPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def update_key_credentials(
            self, object_id, value=None, custom_headers=None, raw=False, **operation_config):
        """Update keyCredentials associated with an existing service principal.
        Reference:
        https://msdn.microsoft.com/en-us/library/azure/ad/graph/api/entity-and-complex-type-reference#keycredential-type.

        :param object_id: Object id to get service principal information.
        :type object_id: str
        :param value: KeyCredential list.
        :type value: list of :class:`KeyCredential
         <azure.graphrbac.models.KeyCredential>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        parameters = models.KeyCredentialsUpdateParameters(value=value)

        # Construct URL
        url = '/{tenantID}/servicePrincipals/{objectId}/keyCredentials'
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'KeyCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list_password_credentials(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Gets passwordCredentials associated with an existing service
        principal. Reference:
        https://msdn.microsoft.com/en-us/library/azure/ad/graph/api/entity-and-complex-type-reference#passwordcredential-type.

        :param object_id: Object id to get service principal information.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`PasswordCredentialPaged
         <azure.graphrbac.models.PasswordCredentialPaged>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/{tenantID}/servicePrincipals/{objectId}/passwordCredentials'
                path_format_arguments = {
                    'objectId': self._serialize.url("object_id", object_id, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.PasswordCredentialPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.PasswordCredentialPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def update_password_credentials(
            self, object_id, value=None, custom_headers=None, raw=False, **operation_config):
        """Updates passwordCredentials associated with an existing service
        principal. Reference:
        https://msdn.microsoft.com/en-us/library/azure/ad/graph/api/entity-and-complex-type-reference#passwordcredential-type.

        :param object_id: Object id to get service principal information.
        :type object_id: str
        :param value: PasswordCredential list.
        :type value: list of :class:`PasswordCredential
         <azure.graphrbac.models.PasswordCredential>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        parameters = models.PasswordCredentialsUpdateParameters(value=value)

        # Construct URL
        url = '/{tenantID}/servicePrincipals/{objectId}/passwordCredentials'
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str', skip_quote=True),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'PasswordCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response