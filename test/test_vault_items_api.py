# coding: utf-8

"""
    Vault Management API

    This schema documents the endpoints available to the Vault Management API, accessible from the Bitwarden CLI using the `bw serve` command ([learn more](https://bitwarden.com/help/cli/)). If you're looking for the **Organization Management** API, refer instead to [this document](https://bitwarden.com/help/api/).

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bw_serve_client.api.vault_items_api import VaultItemsApi  # noqa: E501


class TestVaultItemsApi(unittest.TestCase):
    """VaultItemsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VaultItemsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_list_object_items_get(self) -> None:
        """Test case for list_object_items_get

        Retrieve a list of items in your vault.  # noqa: E501
        """
        pass

    def test_object_item_id_delete(self) -> None:
        """Test case for object_item_id_delete

        Delete an item from your vault.  # noqa: E501
        """
        pass

    def test_object_item_id_get(self) -> None:
        """Test case for object_item_id_get

        Retrieve an item from your vault.  # noqa: E501
        """
        pass

    def test_object_item_id_put(self) -> None:
        """Test case for object_item_id_put

        Edit an item in your Vault.  # noqa: E501
        """
        pass

    def test_object_item_post(self) -> None:
        """Test case for object_item_post

        Add a new item to your vault.  # noqa: E501
        """
        pass

    def test_restore_item_id_post(self) -> None:
        """Test case for restore_item_id_post

        Restore a deleted item.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
