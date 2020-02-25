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

    def testList(self):
        expected = [0, 0]
        self.assertEqual(expected, task.getitems([0]))
        expected = [0, 5]
        self.assertEqual(expected, task.getitems([0, 1, 2, 3, 4, 5]))

    def testDates(self):
        expected = 1
        self.assertEqual(expected, task.findDateRange("08/02/2020", "08/03/2020"))


if __name__ == '__main__':
    unittest.main()
