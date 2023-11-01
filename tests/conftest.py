import pytest
from unittest.mock import MagicMock
import schema_parser


@pytest.fixture
def simple_schema():
    return {
        "profile": {
            "count": 100,
            "index": "profile",
            "properties": {
                "id": {
                    "type": "increment",
                    "start": 1,
                    "step": 1,
                    "blank_percent": 0,
                    "format": "lambda x: str(x).zfill(5)"
                },
                "name": {
                    "type": "full_name"
                }
            }
        }
    }


@pytest.fixture
def mock_read_file(monkeypatch):
    my_mock = MagicMock()
    monkeypatch.setattr(schema_parser.utils, "read_json_file", my_mock)
    return my_mock
