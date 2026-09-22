import unittest

from dnr_quant.shared.hashing.sha256 import sha256_bytes, sha256_utf8


class Sha256Test(unittest.TestCase):
    def test_utf8_and_bytes_match(self) -> None:
        value = "DNR"
        self.assertEqual(sha256_bytes(value.encode("utf-8")), sha256_utf8(value))


if __name__ == "__main__":
    unittest.main()
