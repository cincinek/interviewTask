#!/usr/bin/env
import unittest
from interview import Interview


class BoxesTest(unittest.TestCase):
    def test_boxes(self):
        obj = Interview()
        with self.assertRaises(ValueError):
            obj.boxes(-1)
            obj.boxes(1000)
            obj.boxes(0)
        with self.assertRaises(TypeError):
            obj.boxes("-adasdasd")

        self.assertEqual(
            obj.boxes(1), {"small": 1, "medium": 0, "large": 0, "common": 0}
        )
        self.assertEqual(
            obj.boxes(3), {"small": 1, "medium": 0, "large": 0, "common": 0}
        )
        self.assertEqual(
            obj.boxes(4), {"small": 0, "medium": 1, "large": 0, "common": 0}
        )
        self.assertEqual(
            obj.boxes(6), {"small": 0, "medium": 1, "large": 0, "common": 0}
        )
        self.assertEqual(
            obj.boxes(13), {"small": 0, "medium": 0, "large": 2, "common": 1}
        )
        self.assertEqual(
            obj.boxes(9), {"small": 0, "medium": 0, "large": 1, "common": 0}
        )
        self.assertEqual(
            obj.boxes(11), {"small": 0, "medium": 2, "large": 0, "common": 1}
        )
        self.assertEqual(
            obj.boxes(19), {"small": 1, "medium": 0, "large": 2, "common": 1}
        )
        self.assertEqual(
            obj.boxes(22), {"small": 0, "medium": 1, "large": 2, "common": 1}
        )
        self.assertEqual(
            obj.boxes(29), {"small": 1, "medium": 0, "large": 3, "common": 2}
        )
        self.assertEqual(
            obj.boxes(36), {"small": 0, "medium": 0, "large": 4, "common": 2}
        )


if __name__ == "__main__":
    unittest.main()
