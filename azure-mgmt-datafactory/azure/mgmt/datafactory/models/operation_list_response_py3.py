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

from msrest.serialization import Model


class OperationListResponse(Model):
    """A list of operations that can be performed by the Data Factory service.

    :param value: List of Data Factory operations supported by the Data
     Factory resource provider.
    :type value: list[~azure.mgmt.datafactory.models.Operation]
    :param next_link: The link to the next page of results, if any remaining
     results exist.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value=None, next_link: str=None, **kwargs) -> None:
        super(OperationListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link