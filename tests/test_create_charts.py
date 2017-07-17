import unittest
import context

from srvy.synch.create_charts import sample_test

class MyTest(unittest.TestCase):
    def test_sample_test(self):
        self.assertEqual(sample_test(1,2), 3)

if __name__ == '__main__':
    unittest.main()