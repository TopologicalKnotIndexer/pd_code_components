import unittest

from pd_code_components import get_components_from_pd_code


class ComponentTests(unittest.TestCase):
    def test_finds_hopf_components_deterministically(self):
        hopf = [[2, 3, 1, 4], [4, 1, 3, 2]]
        self.assertEqual(get_components_from_pd_code(hopf), [[1, 2], [3, 4]])

    def test_accepts_empty_unknot_code(self):
        self.assertEqual(get_components_from_pd_code([]), [])

    def test_rejects_bad_counts_and_mixed_types(self):
        with self.assertRaisesRegex(ValueError, "exactly twice"):
            get_components_from_pd_code([[1, 2, 3, 4]])
        with self.assertRaisesRegex(TypeError, "consistent"):
            get_components_from_pd_code([[1, 1, "2", "2"]])


if __name__ == "__main__":
    unittest.main()
