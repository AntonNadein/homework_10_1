import unittest
from unittest.mock import patch

from src.selection_cycles import triple_question, while_true_question


class TestWhileTrueQuestion(unittest.TestCase):

    @patch(
        "builtins.input", side_effect=["sdcddw", "yes", "no", "exit", "lwlwv"]
    )
    def test_while_true_question(self, mock_input):
        result = while_true_question("Do you agree?", "yes", "no")
        self.assertEqual(result, "yes")

        result = while_true_question("Do you agree?", "yes", "no")
        self.assertEqual(result, "no")

        result = while_true_question("Do you agree?", "yes", "no")
        self.assertIsNone(result)

        # result = while_true_question("Do you agree?", "yes", "no")
        # self.assertIsNone(result, "Введите yes или no\n")


class TestTripleQuestion(unittest.TestCase):

    @patch(
        "builtins.input",
        side_effect=[
            "122",
            "sdcddw",
            "one",
            "two",
            "three",
            "exit",
            "155",
            "1",
            "2",
            "3",
            "0",
        ],
    )
    def test_triple_question(self, mock_input):
        result = triple_question("Count to three", "one", "two", "three")
        self.assertEqual(result, "one")

        result = triple_question("Count to three?", "one", "two", "three")
        self.assertEqual(result, "two")

        result = triple_question("Count to three?", "one", "two", "three")
        self.assertEqual(result, "three")

        result = triple_question("Count to three?", "one", "two", "three")
        self.assertIsNone(result, None)

        result = triple_question("Count to three", 1, 2, 3)
        self.assertEqual(result, 1)

        result = triple_question("Count to three", 1, 2, 3)
        self.assertEqual(result, 2)

        result = triple_question("Count to three", 1, 2, 3)
        self.assertEqual(result, 3)

        result = triple_question("Count to three", 1, 2, 3)
        self.assertIsNone(result, None)
