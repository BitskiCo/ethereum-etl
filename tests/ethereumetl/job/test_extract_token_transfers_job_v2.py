import csv
import io

import pytest

import tests.resources
from ethereumetl.jobs.exporters.token_transfers_v2_item_exporter import token_transfers_v2_item_exporter
from ethereumetl.jobs.extract_token_transfers_v2_job import ExtractTokenTransfersV2Job
from tests.helpers import compare_lines_ignore_order, read_file

RESOURCE_GROUP = 'test_extract_token_transfers_job_v2'


def read_resource(resource_group, file_name):
    return tests.resources.read_resource([RESOURCE_GROUP, resource_group], file_name)


@pytest.mark.parametrize('resource_group', [
    'logs'
])
def test_export_token_transfers_job(tmpdir, resource_group):
    output_file = str(tmpdir.join('token_transfers_v2.csv'))

    logs_content = read_resource(resource_group, 'logs.csv')
    logs_csv_reader = csv.DictReader(io.StringIO(logs_content))
    job = ExtractTokenTransfersV2Job(
        logs_iterable=logs_csv_reader,
        batch_size=2,
        item_exporter=token_transfers_v2_item_exporter(output_file),
        max_workers=5
    )
    job.run()

    compare_lines_ignore_order(
        read_resource(resource_group, 'expected_token_transfers_v2.csv'), read_file(output_file)
    )
