import unittest
from random import Random
from unittest.mock import patch

from part_3.cat import Cat


class TestCatAge(unittest.TestCase):
    @patch('part_3.cat.random')
    def test_age_with_random_seed_always_is_6(self, random):
        self.random = Random(1)
        random.randint._mock_side_effect = self.random.randint
        cat = Cat()
        self.assertEqual(6, cat.getAge())

    @unittest.mock.patch('part_3.cat.random')
    def test_cat_age_gets_a_random_integer_in_the_range(self, mock_random):
        _ = Cat()
        mock_random.randint.assert_called_with(5, 10)

    def test_age_is_between_5_and_10(self):
        cat = Cat()
        self.assertLessEqual(cat.getAge(), 10)
        self.assertGreaterEqual(cat.getAge(), 5)


class TestCatSpeak(unittest.TestCase):
    @patch('builtins.print')
    def test_speak_calls_print_with_meow_if_no_arg_specified(self, mock_print):
        # There's a couple ways to do this one
        cat = Cat()
        cat.speak()
        mock_print.assert_called_with('meow')

    @patch('builtins.print')
    def test_speak_calls_print_with_arg_if_arg_specified(self, mock_print):
        # There's a couple ways to do this one
        cat = Cat()
        cat.speak('hello human, as you can see I can talk now')
        mock_print.assert_called_with('hello human, as you can see I can talk now')

    @patch('builtins.print')
    def test_calling_speak_1_to_4_times_does_not_increase_age(self, _):
        cat = Cat()
        initialAge = 1
        cat.setAge(initialAge)
        for i in range(0, 4):
            self.assertEqual(1, cat.getAge())
            cat.speak()

    @patch('builtins.print')
    def test_calling_speak_5_times_increases_age_by_1(self, _):
        cat = Cat()
        initialAge = 1
        cat.setAge(initialAge)
        for i in range(0, 5):
            cat.speak()
        self.assertEqual(2, cat.getAge())
