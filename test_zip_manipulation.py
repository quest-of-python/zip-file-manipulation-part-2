import pathlib
import unittest

from zip_manipulation import retrieve_sum_from_uuids


class TestZipManipulation(unittest.TestCase):
    def test_retrieve_sum_from_uuids(self):
        zip_path = pathlib.Path("archive.zip")

        self.assertEqual(
            retrieve_sum_from_uuids(zip_path=zip_path),
            45953,
        )


if __name__ == '__main__':
    unittest.main()
