import collections
import json
import logging
import os

from kafka import KafkaProducer

from blockchainetl.jobs.exporters.converters.composite_item_converter import CompositeItemConverter


class KafkaItemExporter:

    def __init__(self, output, item_type_to_topic_mapping, converters=()):
        self.item_type_to_topic_mapping = item_type_to_topic_mapping
        self.converter = CompositeItemConverter(converters)
        self.connection_url = self.get_connection_url(output)
        print(self.connection_url)

        self.producer = self.determine_and_connect_kafka(self.connection_url)

    @staticmethod
    def determine_and_connect_kafka(connection_url):
        kafka_sasl_mechanism = os.environ.get("KAFKA_SASL_MECHANISMS")
        security_protocol = os.environ.get("KAFKA_SECURITY_PROTOCOL")
        kafka_username = os.environ.get("KAFKA_USERNAME")
        kafka_password = os.environ.get("KAFKA_PASSWORD")

        if None in [kafka_sasl_mechanism, security_protocol, kafka_username, kafka_password]:
            return KafkaProducer(bootstrap_servers=connection_url)
        else:
            return KafkaProducer(bootstrap_servers=connection_url,
                                 sasl_plain_username=kafka_username,
                                 sasl_plain_password=kafka_password,
                                 sasl_mechanism=kafka_sasl_mechanism,
                                 security_protocol=security_protocol)

    def get_connection_url(self, output):
        try:
            return output.split('/')[1]
        except KeyError:
            raise Exception('Invalid kafka output param, It should be in format of "kafka/127.0.0.1:9092"')

    def open(self):
        pass

    def export_items(self, items):
        for item in items:
            self.export_item(item)

    def export_item(self, item):
        item_type = item.get('type')
        if item_type is not None and item_type in self.item_type_to_topic_mapping:
            item = self.converter.convert_item(item)
            data = json.dumps(item).encode('utf-8')
            print(data)
            return self.producer.send(self.item_type_to_topic_mapping[item_type], value=data)
        else:
            logging.warning('Topic for item type "{}" is not configured.'.format(item_type))

    def convert_items(self, items):
        for item in items:
            yield self.converter.convert_item(item)

    def close(self):
        pass


def group_by_item_type(items):
    result = collections.defaultdict(list)
    for item in items:
        result[item.get('type')].append(item)

    return result
