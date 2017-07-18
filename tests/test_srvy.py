import unittest
import context

from srvy.srvy import pull_questions_from_csv


class MyTest(unittest.TestCase):
    def setUp(self):
        self.csv_questions = ["Question 1?", "Question 2?", "Question 3?", "Question 4?"]

    def test_pull_questions_from_csv(self):
        self.assertEqual(pull_questions_from_csv('questions.csv'), self.csv_questions)


if __name__ == '__main__':
    unittest.main()