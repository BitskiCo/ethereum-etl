from ethereumetl.domain.receipt_log import EthReceiptLog
from ethereumetl.service.token_transfer_v2_extractor import EthTokenTransferV2Extractor

token_transfer_extractor = EthTokenTransferV2Extractor()



def test_extract_transfer_from_receipt_log_erc20():
    log = EthReceiptLog()
    log.address = '0x25c6413359059694A7FCa8e599Ae39Ce1C944Da2'
    log.block_number = 1061946
    log.log_index = 0
    log.topics = ['0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960',
                  '0x0000000000000000000000000000000000000000000000000000000000000000',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960']
    log.data = '0x00000000000000000000000000000000000000000000000000000000000000090000000000000000000000000000000000000000000000000000000000000001'
    log.transaction_hash = '0xd62a74c7b04e8e0539398f6ba6a5eb11ad8aa862e77f0af718f0fad19b0b0480'

    token_transfers = token_transfer_extractor.extract_transfer_from_log(log)

    

def test_extract_transfer_from_receipt_log_erc720():
    log = EthReceiptLog()
    log.address = '0x25c6413359059694A7FCa8e599Ae39Ce1C944Da2'
    log.block_number = 1061946
    log.log_index = 0
    log.topics = ['0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960',
                  '0x0000000000000000000000000000000000000000000000000000000000000000',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960']
    log.data = '0x00000000000000000000000000000000000000000000000000000000000000090000000000000000000000000000000000000000000000000000000000000001'
    log.transaction_hash = '0xd62a74c7b04e8e0539398f6ba6a5eb11ad8aa862e77f0af718f0fad19b0b0480'

    token_transfers = token_transfer_extractor.extract_transfer_from_log(log)

    

def test_extract_transfer_from_receipt_log_erc1155_single():
    log = EthReceiptLog()
    log.address = '0x25c6413359059694A7FCa8e599Ae39Ce1C944Da2'
    log.block_number = 1061946
    log.log_index = 0
    log.topics = ['0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960',
                  '0x0000000000000000000000000000000000000000000000000000000000000000',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960']
    log.data = '0x00000000000000000000000000000000000000000000000000000000000000090000000000000000000000000000000000000000000000000000000000000001'
    log.transaction_hash = '0xd62a74c7b04e8e0539398f6ba6a5eb11ad8aa862e77f0af718f0fad19b0b0480'

    token_transfers = token_transfer_extractor.extract_transfer_from_log(log)

    


def test_extract_transfer_from_receipt_log_erc1155_batch():
    log = EthReceiptLog()
    log.address = '0x25c6413359059694A7FCa8e599Ae39Ce1C944Da2'
    log.block_number = 1061946
    log.log_index = 0
    log.topics = ['0x4a39dc06d4c0dbc64b70af90fd698a233a518aa5d07e595d983b8c0526c8f7fb',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960',
                  '0x0000000000000000000000000000000000000000000000000000000000000000',
                  '0x0000000000000000000000009056d15c49b19df52ffad1e6c11627f035c0c960']
    log.data = '0x00000000000000000000000000000000000000000000000000000000000000090000000000000000000000000000000000000000000000000000000000000001'
    log.transaction_hash = '0xd62a74c7b04e8e0539398f6ba6a5eb11ad8aa862e77f0af718f0fad19b0b0480'

    token_transfers = token_transfer_extractor.extract_transfer_from_log(log)

