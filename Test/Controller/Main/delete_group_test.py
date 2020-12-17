import io
import unittest
from unittest.mock import patch


def convert_input_to_int(user_input: str):
    try:
        val = int(user_input)
        return val
    except ValueError:
        raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")


def delete_group_logic(cmd_input: str, groups_count: int):
    if cmd_input == "":
        raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")
    cmd_input = convert_input_to_int(cmd_input)
    if cmd_input == 0:
        print("0 - Выход\n",
              "1 - Студент\n",
              "2 - Группа\n",
              "3 - Предмет\n",
              "4 - БРС", sep="")
    elif cmd_input <= groups_count:
        print("Успешно удален\n",
              "0. Назад")
    else:
        raise Exception("Выход за пределы массива ( ´•︵•` )")


class DeleteGroupTestCase(unittest.TestCase):
    def setUp(self):
        self.groups = [["М-ФИИТ", 2020], ["М-ИВТ", 2020]]
        self.cmd_input = ["1"]
        self.success_output = "Успешно удален\n" \
                              " 0. Назад"
        self.back_output = "0 - Выход\n" \
                           "1 - Студент\n" \
                           "2 - Группа\n" \
                           "3 - Предмет\n" \
                           "4 - БРС"

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_0(self, mock_obj):
        # given setUp
        with patch('builtins.input', side_effect=self.cmd_input):
            cmd_input = input()
            groups_count = len(self.groups)
            # when
            delete_group_logic(cmd_input, groups_count)

        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.success_output, result)

    def test_case_1(self):
        # given
        self.groups = []
        with patch('builtins.input', side_effect=self.cmd_input):
            cmd_input = input()
            groups_count = len(self.groups)
            # then
            with self.assertRaises(Exception):
                # when
                raise delete_group_logic(cmd_input, groups_count)

    def test_case_2(self):
        # given
        self.cmd_input = ["3"]
        with patch('builtins.input', side_effect=self.cmd_input):
            cmd_input = input()
            groups_count = len(self.groups)
            # then
            with self.assertRaises(Exception):
                # when
                raise delete_group_logic(cmd_input, groups_count)

    def test_case_3(self):
        # given
        self.cmd_input = ["two"]
        with patch('builtins.input', side_effect=self.cmd_input):
            cmd_input = input()
            groups_count = len(self.groups)
            # then
            with self.assertRaises(Exception):
                # when
                raise delete_group_logic(cmd_input, groups_count)

    def test_case_4(self):
        # given
        self.cmd_input = [""]
        with patch('builtins.input', side_effect=self.cmd_input):
            cmd_input = input()
            groups_count = len(self.groups)
            print(cmd_input)
            # then
            with self.assertRaises(Exception):
                # when
                raise delete_group_logic(cmd_input, groups_count)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_case_5(self, mock_obj):
        # given
        self.cmd_input = ['0']
        with patch('builtins.input', side_effect=self.cmd_input):
            cmd_input = input()
            groups_count = len(self.groups)
            # when
            delete_group_logic(cmd_input, groups_count)
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.back_output, result)
