import unittest
import sys
import os

file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_path)
from function_lib.customers.customer import Customer
from function_lib.rights_management.management import RightManagement
from function_lib.rights_management.management import User_id


class Customer_case(unittest.TestCase):

    def setUp(self) -> None:
        """
        self.customer_operation_permissions  客户模块操作权限
        self.customer_transfer_permissions   转移客户权限
        self.customer_id_list                获取前100个客户的列表
        self.my_user                         当前用户信息
        self.customer_id                     获取100个客户的id
        self.user_id                         获取当前用户id
        :return:
        """
        self.customer_operation_permissions = RightManagement().permission('customer')
        self.customer_transfer_permissions = Customer.customers_permissions()
        self.customer_id_list = Customer.get_customers_id(100)
        self.my_user = User_id.my_user_id()
        self.customer_id = self.customer_id_list.json()['data']['list'][0]['id']
        self.user_id = self.my_user.json()['data']['users'][0]['id']

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
            print(res.status_code)
            self.assertEqual(res.status_code, 200)
        else:
            print(res.status_code)
            self.assertEqual(res.status_code, 401)

    def test003(self):
        """
        判断客户是否有转移权限
        :return:
        """
        print(self.customer_id, self.user_id)
        res = Customer.transfer_customers_one(self.customer_id, self.user_id)
        if 'transfer' in self.customer_operation_permissions:
            print(res.status_code)
            self.assertEqual(res.status_code, 200)
        else:
            self.assertEqual(res.status_code, 401)

    def test004(self):
        """
        判断客户是否有编辑权限
        :return:
        """
        pass


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Customer_case('test003'))
    unittest.TextTestRunner(verbosity=2).run(test_suite)