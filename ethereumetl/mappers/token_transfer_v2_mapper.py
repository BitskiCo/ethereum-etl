
class EthTokenTransferV2Mapper(object):
    def token_transfer_to_dict(self, token_transfer_v2):
        return {
            'type': 'token_transfer',
            'token_address': token_transfer_v2.token_address,
            'from_address': token_transfer_v2.from_address,
            'to_address': token_transfer_v2.to_address,
            'value': token_transfer_v2.value,
            'transaction_hash': token_transfer_v2.transaction_hash,
            'log_index': token_transfer_v2.log_index,
            'block_number': token_transfer_v2.block_number,
        }
