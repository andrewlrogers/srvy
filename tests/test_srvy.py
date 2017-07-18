import unittest
import context

from srvy.srvy import get_current_questions


class MyTest(unittest.TestCase):
    def setUp(self):
        self.questions = ["Question 1?", "Question 2?", "Question 3?", "Question 4?"]

    def test_get_current_questions_gets_all_questions_from_file(self):
        self.assertEqual(get_current_questions('questions.txt'), self.questions)


if __name__ == '__main__':
    unittest.main()
