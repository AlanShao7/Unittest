import unittest
import sys
import os
file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_path)
from function_lib.customers.customer import Customer
from function_lib.rights_management.management import RightManagement


class Customer_case(unittest.TestCase):

    def setUp(self) -> None:
        self.customer_operation_permissions = RightManagement().permission('customer')
        self.customer_transfer_permissions = Customer.customers_permissions()

    def test001(self):
        """
        判断权限获取是否正确问题
        :return:
        """
        self.assertEqual(self.customer_transfer_permissions.json()['code'], '0')

    def test002(self):
        """
        判断权限和新增问题
        有权限200  没权限401
        :return:
        """
        res = Customer.add_customer_one('ceshi')
        if 'create' in self.customer_operation_permissions:
            # print(res.status_code)
            self.assertEqual(res.status_code, 200)
        else:
            # print(res.status_code)
            self.assertEqual(res.status_code, 401)


if __name__ == '__main__':
    a = Customer_case()