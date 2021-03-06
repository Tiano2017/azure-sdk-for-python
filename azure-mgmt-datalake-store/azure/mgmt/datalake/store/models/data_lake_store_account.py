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

from .resource import Resource


class DataLakeStoreAccount(Resource):
    """Data Lake Store account information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar location: The resource location.
    :vartype location: str
    :ivar tags: The resource tags.
    :vartype tags: dict[str, str]
    :ivar identity: The Key Vault encryption identity, if any.
    :vartype identity: ~azure.mgmt.datalake.store.models.EncryptionIdentity
    :ivar account_id: The unique identifier associated with this Data Lake
     Store account.
    :vartype account_id: str
    :ivar provisioning_state: The provisioning status of the Data Lake Store
     account. Possible values include: 'Failed', 'Creating', 'Running',
     'Succeeded', 'Patching', 'Suspending', 'Resuming', 'Deleting', 'Deleted',
     'Undeleting', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.datalake.store.models.DataLakeStoreAccountStatus
    :ivar state: The state of the Data Lake Store account. Possible values
     include: 'Active', 'Suspended'
    :vartype state: str or
     ~azure.mgmt.datalake.store.models.DataLakeStoreAccountState
    :ivar creation_time: The account creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: The account last modified time.
    :vartype last_modified_time: datetime
    :ivar endpoint: The full CName endpoint for this account.
    :vartype endpoint: str
    :ivar default_group: The default owner group for all new folders and files
     created in the Data Lake Store account.
    :vartype default_group: str
    :ivar encryption_config: The Key Vault encryption configuration.
    :vartype encryption_config:
     ~azure.mgmt.datalake.store.models.EncryptionConfig
    :ivar encryption_state: The current state of encryption for this Data Lake
     Store account. Possible values include: 'Enabled', 'Disabled'
    :vartype encryption_state: str or
     ~azure.mgmt.datalake.store.models.EncryptionState
    :ivar encryption_provisioning_state: The current state of encryption
     provisioning for this Data Lake Store account. Possible values include:
     'Creating', 'Succeeded'
    :vartype encryption_provisioning_state: str or
     ~azure.mgmt.datalake.store.models.EncryptionProvisioningState
    :ivar firewall_rules: The list of firewall rules associated with this Data
     Lake Store account.
    :vartype firewall_rules:
     list[~azure.mgmt.datalake.store.models.FirewallRule]
    :ivar firewall_state: The current state of the IP address firewall for
     this Data Lake Store account. Possible values include: 'Enabled',
     'Disabled'
    :vartype firewall_state: str or
     ~azure.mgmt.datalake.store.models.FirewallState
    :ivar firewall_allow_azure_ips: The current state of allowing or
     disallowing IPs originating within Azure through the firewall. If the
     firewall is disabled, this is not enforced. Possible values include:
     'Enabled', 'Disabled'
    :vartype firewall_allow_azure_ips: str or
     ~azure.mgmt.datalake.store.models.FirewallAllowAzureIpsState
    :ivar trusted_id_providers: The list of trusted identity providers
     associated with this Data Lake Store account.
    :vartype trusted_id_providers:
     list[~azure.mgmt.datalake.store.models.TrustedIdProvider]
    :ivar trusted_id_provider_state: The current state of the trusted identity
     provider feature for this Data Lake Store account. Possible values
     include: 'Enabled', 'Disabled'
    :vartype trusted_id_provider_state: str or
     ~azure.mgmt.datalake.store.models.TrustedIdProviderState
    :ivar new_tier: The commitment tier to use for next month. Possible values
     include: 'Consumption', 'Commitment_1TB', 'Commitment_10TB',
     'Commitment_100TB', 'Commitment_500TB', 'Commitment_1PB', 'Commitment_5PB'
    :vartype new_tier: str or ~azure.mgmt.datalake.store.models.TierType
    :ivar current_tier: The commitment tier in use for the current month.
     Possible values include: 'Consumption', 'Commitment_1TB',
     'Commitment_10TB', 'Commitment_100TB', 'Commitment_500TB',
     'Commitment_1PB', 'Commitment_5PB'
    :vartype current_tier: str or ~azure.mgmt.datalake.store.models.TierType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'tags': {'readonly': True},
        'identity': {'readonly': True},
        'account_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'endpoint': {'readonly': True},
        'default_group': {'readonly': True},
        'encryption_config': {'readonly': True},
        'encryption_state': {'readonly': True},
        'encryption_provisioning_state': {'readonly': True},
        'firewall_rules': {'readonly': True},
        'firewall_state': {'readonly': True},
        'firewall_allow_azure_ips': {'readonly': True},
        'trusted_id_providers': {'readonly': True},
        'trusted_id_provider_state': {'readonly': True},
        'new_tier': {'readonly': True},
        'current_tier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'EncryptionIdentity'},
        'account_id': {'key': 'properties.accountId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'DataLakeStoreAccountStatus'},
        'state': {'key': 'properties.state', 'type': 'DataLakeStoreAccountState'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'default_group': {'key': 'properties.defaultGroup', 'type': 'str'},
        'encryption_config': {'key': 'properties.encryptionConfig', 'type': 'EncryptionConfig'},
        'encryption_state': {'key': 'properties.encryptionState', 'type': 'EncryptionState'},
        'encryption_provisioning_state': {'key': 'properties.encryptionProvisioningState', 'type': 'EncryptionProvisioningState'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[FirewallRule]'},
        'firewall_state': {'key': 'properties.firewallState', 'type': 'FirewallState'},
        'firewall_allow_azure_ips': {'key': 'properties.firewallAllowAzureIps', 'type': 'FirewallAllowAzureIpsState'},
        'trusted_id_providers': {'key': 'properties.trustedIdProviders', 'type': '[TrustedIdProvider]'},
        'trusted_id_provider_state': {'key': 'properties.trustedIdProviderState', 'type': 'TrustedIdProviderState'},
        'new_tier': {'key': 'properties.newTier', 'type': 'TierType'},
        'current_tier': {'key': 'properties.currentTier', 'type': 'TierType'},
    }

    def __init__(self):
        super(DataLakeStoreAccount, self).__init__()
        self.identity = None
        self.account_id = None
        self.provisioning_state = None
        self.state = None
        self.creation_time = None
        self.last_modified_time = None
        self.endpoint = None
        self.default_group = None
        self.encryption_config = None
        self.encryption_state = None
        self.encryption_provisioning_state = None
        self.firewall_rules = None
        self.firewall_state = None
        self.firewall_allow_azure_ips = None
        self.trusted_id_providers = None
        self.trusted_id_provider_state = None
        self.new_tier = None
        self.current_tier = None
