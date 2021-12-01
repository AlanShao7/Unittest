import unittest
import os
import time
import sys
import HTMLTestRunner
file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_path)
from case_lib.customers.customers_case import Customer_case


def html_report_folder_path(folder_name):
    _current_folder_path = os.getcwd()
    _html_report_folder_path = _current_folder_path + '\\' + folder_name
    is_folder_existed = os.path.exists(_html_report_folder_path)
    if is_folder_existed:
        return _html_report_folder_path
    else:
        os.makedirs(_html_report_folder_path)
        return _html_report_folder_path


def test_cases_set():
    test_suite = unittest.TestSuite()
    # 输入class的地址
    test_suite.addTest(unittest.makeSuite(Customer_case))
    # print(test_suite)

    return test_suite


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    _folder_path = html_report_folder_path(folder_name='HtmlTestReports接口自动化测试报告')
    _html_report_file_abspath = os.path.join(_folder_path, u'接口自动化测试报告_' + now + '.html')

    fp = open(_html_report_file_abspath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title=u'接口自动化测试报告-测试结果展示',
                                           description=u'测试用例执行情况如下：')
    runner.run(test_cases_set())
    fp.close()
