import sys

import utils


def parse_properties_dict(props: dict):
    properties: list[Property] = []
    for key, value in props.items():
        properties.append(Property(key,
                                   value["type"],
                                   {k: v for k, v in value.items() if k != "type"}))
    return properties


def parse_schema_data(index, schema_data):
    try:
        return Schema(index,
                      schema_data["count"],
                      schema_data["index"],
                      parse_properties_dict(schema_data["properties"]))
    except KeyError as ke:
        print("Incorrect schema file:", ke)
        sys.exit(1)


def generate_schemas(filename):
    schemas = []
    _file = utils.read_json_file(filename)
    for _index, _schema in _file.items():
        schemas.append(parse_schema_data(_index, _schema))

    return schemas


class Property:

    def __init__(self, name, prop_type, parameters):
        self.name = name
        self.type = prop_type
        self.parameters = parameters

    def __repr__(self):
        return f"{self.name} ({self.type})"


class Schema:

    def validate_schema(self):
        pass

    def __init__(self, name, count, es_index, properties: list[Property]):
        self.name = name
        self.count = count
        self.es_index = es_index
        self.properties = properties

    def __repr__(self):
        return f"{self.name} - Count: {self.count}, Properties: {self.properties}"

    # def get_indexes(self) -> [str]:
    #     return self.schema.keys()
    #
    # def get_records_to_generate(self, index) -> int:
    #     return self.schema[index].get('count', 1000)
    #
    # def get_index_schema(self, index) -> dict:
    #     return self.schema[index]
    #
    # def get_properties(self, index) -> [str]:
    #     return self.schema[index]['schema'].keys()
    #
    # def get_property(self, index, property) -> dict:
    #     return self.schema[index]['schema'][property]
