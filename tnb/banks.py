from tnb.base_client import BaseClient


class Bank(BaseClient):
    def fetch_accounts(self):
        """
        Fetch accounts from a Bank
        Return response as Python object
        """
        return self.fetch('/accounts')

    def fetch_bank_transactions(self):
        """
        Get transactions from a Bank
        Return response as Python object
        """
        return self.fetch('/bank_transactions')

    def fetch_invalid_blocks(self):
        """
        Get invalid block from a Bank
        Return response as Python object
        """
        return self.fetch('/invalid_blocks')

    def fetch_validators(self):
        """
        Get validators from a Bank
        Return response as Python object
        """
        return self.fetch('/validators')

    def patch_account(self, account_number, node_id, trust, signature):
        """
        Send a PATCH request of an account to a Bank

        :param account_number: Specify the account will be patched
        :param node_id: The Node Identifier of the Bank
        :param trust: The value assigned to trust level of an account
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        resource = f'/accounts/{account_number}'
        body = {
            "message": {
                "trust": trust
            },
            "node_identifier": node_id,
            "signature": signature
        }

        return self.patch(resource, body=body)

    def post_invalid_blocks(self, message, node_id, signature):
        """
        Send a POST request of an invalid block to a Bank

        :param message: Original block, block identifier, and primary validator NID
        :param node_id: Validators node identifier
        :param signature: Hex value of the signed message

        Return response as Python object
        """

        body = {
            "message": {
                "block": {
                    "account_number": "0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb",
                    "message": {
                        "balance_key": "ce51f0d9facaa7d3e69657429dd3f961ce70077a8efb53dcda508c7c0a19d2e3",
                        "txs": [
                            {
                                "amount": 12.5,
                                "recipient": "484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbc"
                            },
                            {
                                "amount": 1,
                                "recipient": "5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8"
                            },
                            {
                                "amount": 4,
                                "recipient": "ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314"
                            }
                        ]
                    },
                    "signature": "ee5a2f2a2f5261c1b633e08dd61182fd0db5604c853ebd8498f6f28ce8e2ccbbc38093918610ea88a7ad47c7f3192ed955d9d1529e7e390013e43f25a5915c0f"
                },
                "block_identifier": "65ae26192dfb9ec41f88c6d582b374a9b42ab58833e1612452d7a8f685dcd4d5",
                "primary_validator_node_identifier": "3afdf37573f1a511def0bd85553404b7091a76bcd79cdcebba1310527b167521"
            },
            "node_identifier": node_id,
            "signature": signature
        }

        return self.post('/invalid_blocks', body=body)

    def connection_requests(self, node_id, signature):
        """
        Send a connection request to a Bank

        :param node_id: The Node Identifier of the Bank
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        body = {
            "message": {
                "ip_address": self.address,
                "port": self.port,
                "protocol": self.protocol
            },
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.post('/connection_requests', body=body)
