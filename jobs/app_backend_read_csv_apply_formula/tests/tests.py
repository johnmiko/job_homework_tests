from json import JSONDecodeError
from unittest import TestCase

from jobs.opus_one.power_calc import clean_json_data, update_key_name, get_data_from_file


class TestGetDataFromFile(TestCase):
    def test_raises_file_not_found_exception_when_file_doesnt_exist(self):
        # 2.) Program can verify that json file exists and is in expected format.
        with self.assertRaises(FileNotFoundError):
            get_data_from_file('./non_existant_file.json')

    def test_raises_json_decode_error_when_file_is_formatted_wrong(self):
        # 2.) Program can verify that json file exists and is in expected format.
        with self.assertRaises(JSONDecodeError):
            get_data_from_file('test_invalid_json_file.json')

    def test_returns_file_content_when_no_exceptions_are_raised(self):
        data = get_data_from_file('test_valid_json.json')
        self.assertEqual(data, {"A": {"B": 1, "C": 2}})


class TestUpdateKeyName(TestCase):
    def test_invalid_key_and_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            update_key_name({'a': {'b': 'c'}}, 'a', 'b')

    def test_invalid_key_raises_value_error(self):
        with self.assertRaises(ValueError):
            update_key_name({'a': {'b': 1}}, 'a', 'b')

    def test_voltage_lowercase_raises_value_error(self):
        with self.assertRaises(ValueError):
            update_key_name({'a': {'voltage': 1}}, 'a', 'voltage')

    def test_voltage_uppercase_is_replaced_with_v(self):
        attempt = update_key_name({'a': {'Voltage': 1}}, 'a', 'Voltage')
        self.assertEqual(attempt, {'a': {'v': 1}})


class TestCleanJsonData(TestCase):
    def test_invalid_key_and_value_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            clean_json_data({'a': {'b': 'c'}})
        self.assertEqual(
            """Data has a key of "b".\n\tKey must be one of ('v', 'V', 'Volts', 'Voltage', 'i', 'I', 'Amps', 'Amperes', 'Current', 'pf', 'PF', 'Power Factor')""",
            str(cm.exception)
        )

    def test_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            clean_json_data({'a': {'Voltage': 'c'}})
        self.assertEqual("""Data has a value of "c" which is type <class 'str'>. Value must be a valid number""",
                         str(cm.exception))

    def test_missing_amps_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            clean_json_data({'a': {'Voltage': 1}})
        self.assertEqual('"a" is missing an amperes value',
                         str(cm.exception))

    def test_missing_voltage_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            clean_json_data({'a': {'Amps': 1}})
        self.assertEqual('"a" is missing a voltage value',
                         str(cm.exception))

    def test_missing_voltage_and_amps_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            clean_json_data({'a': {}})
        self.assertEqual('"a" is missing a voltage value',
                         str(cm.exception))
