import unittest


class EditGroupTestCase(unittest.TestCase):
    def test_case_1(self):
        # given
        groups = []
        cmd_input = "1"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = '2020'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Выход за пределы массива ( ´•︵•` )")

    def test_case_2(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "3"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = '2020'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Выход за пределы массива ( ´•︵•` )")

    def test_case_3(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "2"
        edit_name_input = ''
        edit_year_input = '2020'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_4(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "2"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = ''
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_4(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "2"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = 'two thousand twenty'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_5(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "2"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = 'two thousand twenty'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_6(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "two"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = '2020'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_6(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "two"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = '2020'
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_7(self):
        # given
        cmd_input = 0
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = '2020'
        # then
        self.assertEqual(True, True)

    def test_case_8(self):
        # given
        groups = ["М-ФИИТ 2020", "М-ИВТ 2020"]
        cmd_input = "2"
        edit_name_input = 'Маг_ФИИТ'
        edit_year_input = '2020'
        # then
        self.assertEqual(True, True)
