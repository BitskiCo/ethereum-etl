from ethereumetl.domain.receipt_log import EthReceiptLog
from ethereumetl.service.token_transfer_v2_extractor import EthTokenTransferV2Extractor

token_transfer_extractor = EthTokenTransferV2Extractor()


def test_extract_transfer_from_receipt_log():
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

    token_transfer = token_transfer_extractor.extract_transfer_from_log(log)

    assert token_transfer.contract_address == '0x25c6413359059694a7fca8e599ae39ce1c944da2'
    assert token_transfer.from_address == '0xe9eeaec75883f0e389a78e2260bfac1776df2f1d'
    assert token_transfer.to_address == '0x0000000000000000000000000000000000000000'
    assert token_transfer.amount == 115792089237316195423570985008687907853269984665640564039457584007913129638936
    assert token_transfer.transaction_hash == '0xd62a74c7b04e8e0539398f6ba6a5eb11ad8aa862e77f0af718f0fad19b0b0480'
    assert token_transfer.block_number == 1061946


test_extract_transfer_from_receipt_log()