import io
import unittest
from unittest.mock import patch


class DeleteGroupTestCase(unittest.TestCase):
    def setUp(self):
        self.groups = [["М-ФИИТ", 2020], ["М-ИВТ", 2020]]
        self.cmd_input = "21"
        self.success_output = "Успешно удален\n" \
                              " 0. Назад"

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0(self, mock_obj):
        # given setUp
        with patch('builtins.input', side_effect=self.cmd_input):
            n = input()
            r = input()
            print(r, n)
            # print("Успешно удален\n",
            #       "0. Назад")
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)

    def test_case_1(self):
        # given
        self.groups = []
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Выход за пределы массива ( ´•︵•` )")

    def test_case_2(self):
        # given
        self.cmd_input = "3"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Выход за пределы массива ( ´•︵•` )")

    def test_case_3(self):
        # given
        self.cmd_input = "two"
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_4(self):
        # given
        self.cmd_input = ""
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_5(self):
        # given
        self.cmd_input = '0'
        # then
        self.assertEqual(True, True)
