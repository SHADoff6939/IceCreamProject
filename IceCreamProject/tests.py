import unittest
import sqlite3
from io import StringIO
import sys

# Припустимо, що ми імпортували ваші функції
from your_module import item_list, cart_price, total_cash_amount  # Замініть your_module на ім'я файлу

class TestIceCreamCounter(unittest.TestCase):
    
    def setUp(self):
        # Налаштування перед кожним тестом (створення тимчасової бази даних)
        self.connection = sqlite3.connect(':memory:')
        self.connection.execute('CREATE TABLE sales (item TEXT, price INTEGER, saled INTEGER);')
        self.connection.commit()
        self.items = [
            ('Вафельний ріжок', 25),
            ('Цукровий ріжок', 35),
            ('Креманка', 40)
        ]
    
    def tearDown(self):
        # Закриття з'єднання після кожного тесту
        self.connection.close()

    def test_cart_price(self):
        cart = [('Вафельний ріжок', 25), ('Цукровий ріжок', 35)]
        self.assertEqual(cart_price(cart), 60)

    def test_total_cash_amount(self):
        with self.connection:
            for item_name, item_price in self.items:
                self.connection.execute("INSERT INTO sales (item, price, saled) VALUES (?, ?, ?)", (item_name, item_price, 1))
        cash = total_cash_amount(self.items, self.connection)
        self.assertEqual(cash, 100)

    def test_item_list(self):
        cart = [('Вафельний ріжок', 25), ('Цукровий ріжок', 35)]
        captured_output = StringIO()  # Створюємо об'єкт для захоплення виводу
        sys.stdout = captured_output   # Перенаправляємо вивід у об'єкт
        item_list(cart)
        sys.stdout = sys.__stdout__  # Повертаємо нормальний вивід
        self.assertIn('1. Вафельний ріжок: 25', captured_output.getvalue())
        self.assertIn('2. Цукровий ріжок: 35', captured_output.getvalue())

    def test_database_insertion(self):
        # Перевірка, чи правильно додаються елементи в базу даних
        with self.connection:
            for item_name, item_price in self.items:
                self.connection.execute("INSERT INTO sales (item, price, saled) VALUES (?, ?, ?)", (item_name, item_price, 0))
            cursor = self.connection.execute("SELECT * FROM sales")
            rows = cursor.fetchall()
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0], ('Вафельний ріжок', 25, 0))

    def test_cart_operations(self):
        # Симуляція додавання та видалення елементів з кошика
        cart = []
        cart.append(self.items[0])
        self.assertEqual(cart, [('Вафельний ріжок', 25)])
        cart.append(self.items[1])
        self.assertEqual(len(cart), 2)
        cart.pop(0)
        self.assertEqual(cart, [('Цукровий ріжок', 35)])

if __name__ == '__main__':
    unittest.main()
