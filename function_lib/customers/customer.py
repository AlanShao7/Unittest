import os
import sys
file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_path)
from function_lib.public_func import HttpRequest


class Customer:

    def __init__(self):
        pass

    @staticmethod
    def customers_permissions():
        """
        获取客户权限
        :return: 客户权限
        """
        api = '/api/pc/customers/permissions'
        res_permissions = HttpRequest().send_request(api, 'get')
        return res_permissions

    @staticmethod
    def get_customers_list(page=1, per_page=10, query='', custom_field_name='', department_id='', sort='', order='', tab_type='', user_id='', status='', category='', real_revisit_at='', product_id=''):
        """
        获取客户列表
        :param page: 页码
        :param per_page: 每页的数量
        :param query: 搜索关键字
        :param custom_field_name: 搜索字段
        :param department_id: 部门id
        :param sort: 排序类型(created_at ), api/v2/customers/filter_sort_group 返回值中sorts的value
        :param order: 排序方式（asc desc）
        :param tab_type: 值为[my, sub, common, assist]或不传
        :param user_id: 员工筛选
        :param status: 状态, 值为 api/v2/customers/status/filter_options返回值
        :param category: 分类
        :param real_revisit_at: 实际跟进时间
        :param product_id: product筛选
        :return: res_list: 客户列表数据
        """
        api = '/api/pc/customers'
        data = {
            "page": page,
            "per_page": per_page,
            "query": query,
            "custom_field_name": custom_field_name,
            "department_id": department_id,
            'sort': sort,
            'order': order,
            'tab_type': tab_type,
            'user_id': user_id,
            'status': status,
            'category': category,
            'real_revisit_at': real_revisit_at,
            'product_id': product_id
        }
        res_list = HttpRequest().send_request(api, 'get', data)
        return res_list

    @staticmethod
    def add_customer_one(name, parent_id='', phone='', tel='', applying_flag='0'):
        """
        新增一个客户
        :param applying_flag: 是否开启审批
        :param name:客户姓名
        :param parent_id:商机客户Id
        :param phone:手机
        :param tel:电话
        :return:新增客户返回结果
        """
        if applying_flag == '0':
            applying = ''
        else:
            applying = 'applying'

        api = '/api/customers'
        data = {
            'customer[name]': name,
            'customer[parent_id]': parent_id,
            'customer[address_attributes][phone]': phone,
            'customer[address_attributes][tel]': tel,
            "customer[approve_status]": applying,
        }
        res = HttpRequest().send_request(api_name=api, method='post', data=data, content_type='application/x-www-form-urlencoded')
        return res

    @staticmethod
    def add_customer_much(count, parent_id='', phone='', tel='', applying_flag='0'):
        """

        :param applying_flag: 是否开启审批 0关闭 1开启
        :param count: 创建客户的个数
        :param parent_id: 商机客户Id
        :param phone: 手机
        :param tel: 电话
        :return:新增客户的返回值列表
        """
        res_list = []
        if applying_flag == '0':
            applying = ''
        else:
            applying = 'applying'
        api = 'api/customers'
        for i in range(count):
            name = '新增客户' + str(i+1)
            data = {
                'customer[name]': name,
                'customer[parent_id]': parent_id,
                'customer[address_attributes][phone]': phone,
                'customer[address_attributes][tel]': tel,
                "customer[approve_status]": applying,
            }
            res = HttpRequest().send_request(api, 'post', data=data)
            res_list.append(res)

        return res_list

    @staticmethod
    def transfer_customers_one(customer_id, user_id, transfer_contracts='false', transfer_opportunities='false', nowin_opportunities='false'):
        """
        转移客户(合同和商机）
        :param customer_id:转移客户的id int
        :param user_id:转移给的负责人 int
        :param transfer_contracts: 是否同时转移客户下的商机(true/false)
        :param transfer_opportunities:是否同时转移客户下的合同(true/false)
        :param nowin_opportunities:是否仅转移未赢单的商机 (true/false), 在transfer_opportunities为true时才需要传递这个参数
        :return:转移客户后的返回结果
        """
        api = '/api/pc/customers/' + customer_id + '/update_user'
        data = {
            'id': customer_id,
            'user_id': user_id,
            'transfer_contracts': transfer_contracts,
            'transfer_opportunities': transfer_opportunities,
            'nowin_opportunities': nowin_opportunities,
        }
        res = HttpRequest().send_request(api, 'put', data=data)
        return res

    # def transfer_customers_much(self, resource_ids: list,  user_id: int, resource_type='Customer', transfer_contracts='false', transfer_opportunities='false', nowin_opportunities='false'):
    #     """
    #     批量转移（默认为转移客户）
    #     :param resource_ids:资源ids
    #     :param user_id:被转移的负责人id
    #     :param resource_type:模块名称（Customer）
    #     :param transfer_contracts:是否转移客户下合同
    #     :param transfer_opportunities:是否转移客户下商机
    #     :param nowin_opportunities:是否只转移客户下未赢单商机
    #     :return: 批量转移结果
    #     """
    #     api = '/api/pc/batch_resources/mass_transfer'
    #     data = {
    #         "resource_type": resource_type,
    #         "resource_ids": resource_ids,
    #         "user_id": user_id,
    #         "transfer_contracts": transfer_contracts,
    #         "transfer_opportunities": transfer_opportunities,
    #         "nowin_opportunities": nowin_opportunities
    #     }
    #     res = HttpRequest().put(data,api)
    #     return res

    @staticmethod
    def check_duplicate(field, field_value, customer_id):
        """
        查重
        :param field:
        :param field_value:
        :param customer_id:
        :return:
        """
        api = '/api/pc/customers/check_duplicate_field'
        data = {
            'field': field,
            'field_value': field_value,
            'customer_id': customer_id
        }
        res = HttpRequest().send_request(api, 'get', data)
        return res


if __name__ == '__main__':
    pass
