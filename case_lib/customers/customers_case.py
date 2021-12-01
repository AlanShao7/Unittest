import unittest
import sys
import os
file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_path)
from function_lib.customers.customer import Customer


class Customer_case(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test001(self):
        """
        判断权限获取是否正确问题
        :return:
        """
        permissions = Customer.customers_permissions()
        print(permissions.json())
        self.assertEqual(permissions.json()['code'], '0')

    def test002(self):
        """

        :return:
        """
        pass


if __name__ == '__main__':
    a = Customer_case()