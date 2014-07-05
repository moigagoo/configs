import unittest

from configs import api
from configs import Config

class TestApi(unittest.TestCase):

    def setUp(self):
        self.sample_config_filename = 'configs/sample.conf'
        self.fallback_config_filename = 'configs/default.conf'
        self.missing_config_filename = 'missing.conf'

    def test_load_general(self):
        """Checks if a valid config file is parsed correctly"""

        self.assertIsInstance(api.load(self.sample_config_filename), Config)

    def test_load_missing_file(self):
        """Checks if the correct exception in raised when a missing config file is attempted to parse"""

        with self.assertRaises(FileNotFoundError):
            api.load(self.missing_config_filename)

    def test_load_check_types(self):
        """Checks automatic float, integer, and boolean value conversion"""

        self.assertIsInstance(api.load(self.sample_config_filename)['list_section'][0], float)
        self.assertIsInstance(api.load(self.sample_config_filename)['list_section'][1], int)
        self.assertIsInstance(api.load(self.sample_config_filename)['mixed']['boolean'], bool)


if __name__ == '__main__':
    unittest.main()
