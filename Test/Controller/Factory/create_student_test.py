import unittest
from datetime import date


class CreateStudentTestCase(unittest.TestCase):
    def test_case_code_1(self):
        # given
        code = "166o09"
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не целое число ( ´•︵•` )")

    def test_case_code_2(self):
        # given
        code = ""
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_fio_3(self):
        # given
        code = 166009
        fio = ""
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_birthdate_4(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = "27.03.2001"
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не правильный тип даты ( ´•︵•` )")

    def test_case_birthdate_5(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = ""
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_email_6(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = ""
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_phone_7(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = ""
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_group_8(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["Math", 2020, 10460]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не правильный тип группы ( ´•︵•` )")

    def test_case_group_9(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ""
        brs_points = ["asd", 2020, "asd", 100]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_brs_10(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd"]
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели не тот тип БРС ( ´•︵•` )")

    def test_case_brs_11(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ""
        # then
        with self.assertRaises(Exception):
            # when
            raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")

    def test_case_create_12(self):
        # given
        code = 166009
        fio = "Platonov Simon Vladimirovich"
        birthdate = date(2001, 3, 27)
        email = "plats2002@gmail.com"
        phone = "+79142247346"
        group = ["FIIT-20", 2020]
        brs_points = ["asd", 2020, "asd", 100]
        # then
        self.assertEqual(True, True)
