import unittest
from sql_concatenator.app import Concatenator

class TestConcatenator(unittest.TestCase):
    def test_concatenate_line_split(self):
        input = 'Hello\nworld\n!'
        expected_output = "('Hello','world','!')"
        actual_output = Concatenator.concatenate(input=input, is_line_split=True, is_custom_split=False, custom_delimiter="")
        self.assertEqual(actual_output, expected_output)

    def test_concatenate_comma_split(self):
        input = 'Hello,world,!'
        expected_output = "('Hello','world','!')"
        actual_output = Concatenator.concatenate(input=input, is_line_split=False, is_custom_split=True, custom_delimiter=",")
        self.assertEqual(actual_output, expected_output)

    def test_concatenate_custom_split(self):
        input = 'Hello123world123!'
        expected_output = "('Hello','world','!')"
        actual_output = Concatenator.concatenate(input=input, is_line_split=False, is_custom_split=True, custom_delimiter="123")
        self.assertEqual(actual_output, expected_output)

    def test_concatenate_custom_split_with_space_and_quotes_and_comma(self):
        input = '798F88D2-0A8C-49BB-AE11-C52B99F410AF", "7D4D9923-003E-4B9D-96C9-A0232CEB1A72", "B5B70DD1-D34F-4494-AE12-59C9F308F001", "6D2A263B-5C8F-41F4-BFBC-623694D671E6'
        expected_output = "('798F88D2-0A8C-49BB-AE11-C52B99F410AF','7D4D9923-003E-4B9D-96C9-A0232CEB1A72','B5B70DD1-D34F-4494-AE12-59C9F308F001','6D2A263B-5C8F-41F4-BFBC-623694D671E6')"
        actual_output = Concatenator.concatenate(input=input, is_line_split=False, is_custom_split=True, custom_delimiter='", "')
        self.assertEqual(actual_output, expected_output)

    def test_concatenate_custom_split_does_not_remove_spaces(self):
        input = 'Hello | world | !'
        expected_output = "('Hello ',' world ',' !')"
        actual_output = Concatenator.concatenate(input=input, is_line_split=False, is_custom_split=True, custom_delimiter="|")
        self.assertEqual(actual_output, expected_output)

    def test_concatenate_line_and_comma_split(self):
        input = 'Hello\n,world\n,!'
        expected_output = "('Hello','world','!')"
        actual_output = Concatenator.concatenate(input=input, is_line_split=True, is_custom_split=True, custom_delimiter=",")
        self.assertEqual(actual_output, expected_output)

def run_tests():
    unittest.main(__name__, argv=['main'], exit=False)