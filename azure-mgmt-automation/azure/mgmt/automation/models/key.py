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


class Key(Model):
    """Automation key which is used to register a DSC Node.

    :param key_name: Automation key name. Possible values include: 'primary',
     'secondary'
    :type key_name: str or ~azure.mgmt.automation.models.AutomationKeyName
    :param permissions: Automation key permissions. Possible values include:
     'Full'
    :type permissions: str or
     ~azure.mgmt.automation.models.AutomationKeyPermissions
    :param value: Value of the Automation Key used for registration.
    :type value: str
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, key_name=None, permissions=None, value=None):
        super(Key, self).__init__()
        self.key_name = key_name
        self.permissions = permissions
        self.value = value