import io
import unittest
from unittest.mock import patch


class PrintMainMenuTestCase(unittest.TestCase):
    def setUp(self):
        self.print_menu = """0 - выход
1 - студент
2 - группа
3 - предмет
4 - БРС"""
        self.year_input = 'Введите год группы:'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_input(self, mock_obj):
        # output
        print("""0 - выход
1 - студент
2 - группа
3 - предмет
4 - БРС""")
        result = mock_obj.getvalue().strip()
        # then
        self.assertEqual(self.print_menu, result)
