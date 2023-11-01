from schema_parser import generate_schemas


class TestSchemaParser:
    def test_simple_schema_parsing(self, simple_schema, mock_read_file):
        mock_read_file.return_value = simple_schema
        schemas = generate_schemas("dummy_file.json")
        print("\nSchemas:\n", schemas)
        assert len(schemas) == 1, "Failed to parse schemas"
