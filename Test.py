# import unittest
# import ddt
#
# data = [{"usename":"zhangsan","pwd":"zhangsan"},{"usename":"lisi","pwd":"lisi"}]
#
# @ddt.ddt
#
# class Testcase(unittest.TestCase):
#
#     @ddt.data(*data)
#     @ddt.unpack
#     def test002(self,usename,pwd):
#         print(data)
#         print("---------------")
#         self.assertEqual(usename+pwd,"zhangsanzhangsan")
#
# if __name__ == '__main__':
#     unittest.main()


# from public_func import HttpRequest
# a = HttpRequest('/api/v2/customers')
# data = {
#             "customer[name]": 'customers'
#         }
# res = a.post(data)
# print(res.text)


# from public_func import HttpRequest
#
# def create(customers):
#     api = HttpRequest('/api/v2/customers')
#     data = {
#         "customer[name]": customers
#     }
#     print(data)
#     res = api.post(data)
#     return res.json()
#
# res = create('ces')
# print(res)
# import unittest
# import ddt
#
# data = (['', '500'], ['测试一下', '200'])
#
# @ddt.ddt
#
# class Testcase(unittest.TestCase):
#
#     @ddt.data(*data)
#     # @ddt.unpack
#     def test002(self,data):
#         print(data)
#         print("---------------")
#         self.assertEqual(data[0],data[1])
#
# if __name__ == '__main__':
#     unittest.main()

# import unittest
# import HTMLTestRunner
#
#
# class TestA(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def test_001(self):
#         print(1)
#         a = 1
#         self.assertEqual(a,2)
#
# if __name__ == '__main__':
#     suiteTest = unittest.TestSuite()
#     suiteTest.addTest(TestA)
#     unittest.TextTestRunner(verbosity=2).run(suiteTest)

#
# import pymysql
# host user passwd charset
# conn = pymysql.connect()

# class ceshi:
#
#     @staticmethod
#     def shishi():
#         print(1)
#
# ceshi.shishi()
# a = 'code'
# assert 'code'
from function_lib.customers.customer import Customer

# res = Customer.get_customers_list()
# print(res.json())
# assert('flag', 2)

resq = Customer.add_customer_one('shao')
if resq.status_code == 0:
    print(resq.json())
else:
    print(resq.status_code)
