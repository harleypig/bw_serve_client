# coding: utf-8

"""
    Vault Management API

    This schema documents the endpoints available to the Vault Management API, accessible from the Bitwarden CLI using the `bw serve` command ([learn more](https://bitwarden.com/help/cli/)). If you're looking for the **Organization Management** API, refer instead to [this document](https://bitwarden.com/help/api/).

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from bw_serve_client.models.item_card import ItemCard  # noqa: E501

class TestItemCard(unittest.TestCase):
    """ItemCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemCard:
        """Test ItemCard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemCard`
        """
        model = ItemCard()  # noqa: E501
        if include_optional:
            return ItemCard(
                brand = 'visa',
                cardholder_name = '',
                code = '',
                exp_month = '',
                exp_year = '',
                number = ''
            )
        else:
            return ItemCard(
        )
        """

    def testItemCard(self):
        """Test ItemCard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
