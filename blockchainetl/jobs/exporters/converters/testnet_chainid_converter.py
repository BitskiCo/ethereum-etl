from blockchainetl.jobs.exporters.converters.simple_item_converter import SimpleItemConverter

class TestnetChainIDConverter(SimpleItemConverter):

    def convert_field(self, key, value):
        if key == 'chain_id':
            return 4
        else:
            return value
