import unittest

from dnr_quant.shared.ids.revision_ref import ExactRevisionRef


class ExactRevisionRefTest(unittest.TestCase):
    def test_parse_requirement_ref(self) -> None:
        ref = ExactRevisionRef.parse("P6-ER-E01-B02-0001@r1")
        self.assertEqual("P6-ER-E01-B02-0001", ref.object_id)
        self.assertEqual(1, ref.revision)
        self.assertEqual("P6-ER-E01-B02-0001@r1", str(ref))

    def test_implicit_latest_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ExactRevisionRef.parse("P6-ER-E01-B02-0001")

    def test_zero_revision_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ExactRevisionRef.parse("P6-ER-E01-B02-0001@r0")


if __name__ == "__main__":
    unittest.main()
