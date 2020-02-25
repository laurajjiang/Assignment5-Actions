import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testArea(self):
        expected = 0
        self.assertEqual(expected, task.findarea(0))
        expected = 12.56
        self.assertEqual(expected, task.findarea(2))


if __name__ == '__main__':
    unittest.main()
