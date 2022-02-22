import json
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
        获取客户权限   转移类型
        :return: 客户权限
        """
        api = '/api/pc/customers/permissions'
        res_permissions = HttpRequest().send_request(api, 'get')
        return res_permissions

    @staticmethod
    def get_customers_list(page=1, per_page=10, query=None,  custom_field_name=None, department_id=None, sort=None, order=None, tab_type=None, user_id=None, status=None, category=None, real_revisit_at=None, product_id=None):
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
    def add_customer_one(name, parent_id=None, phone=None, tel=None, applying_switch=0):
        """
        新增一个客户
        :param applying_switch: 是否开启审批 0关闭 1开启
        :param name:客户姓名
        :param parent_id:商机客户Id
        :param phone:手机
        :param tel:电话
        :return:新增客户返回结果
        """
        applying = '' if applying_switch == 0 else 'applying'

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
    def add_customer_much(count, parent_id=None, phone=None, tel=None, applying_switch=0):
        """

        :param applying_switch: 是否开启审批 0关闭 1开启
        :param count: 创建客户的个数
        :param parent_id: 商机客户Id
        :param phone: 手机
        :param tel: 电话
        :return:新增客户的返回值列表
        """
        res_list = []
        applying = '' if applying_switch == 0 else 'applying'
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
        api = '/api/pc/customers/' + str(customer_id) + '/update_user'
        data = {
            'id': customer_id,
            'user_id': user_id,
            'transfer_contracts': transfer_contracts,
            'transfer_opportunities': transfer_opportunities,
            'nowin_opportunities': nowin_opportunities,
        }
        res = HttpRequest().send_request(api, 'put', json=data)
        if res.status_code != 200:
            print(res.status_code)
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

    @staticmethod
    def get_customers_id(batch_size: int, query=None, custom_field_name=None, department_id=None, sort=None, order=None, tab_type=None, user_id=None, status=None, category=None, real_revisit_at=None, product_id=None):
        """

        :param batch_size: 批量获取条数 200, 500, 1000
        :param query:String	搜索关键字
        :param custom_field_name:String	搜索字段
        :param department_id:Long	部门id
        :param sort:String	排序类型(created_at ), api/v2/customers/filter_sort_group 返回值中sorts的value
        :param order:String	排序方式（asc desc）
        :param tab_type:String	值为[my, sub, common, assist]或不传
        :param user_id:Long	员工筛选
        :param status:Long	状态, 值为 api/v2/customers/status/filter_options返回值
        :param category:Long	分类
        :param real_revisit_at:String	实际跟进时间
        :param product_id:Long	product筛选
        :return:返回请求值，   获取id_list   res['data']
        """
        data = {
            'batch_size': batch_size,
            'query': query,
            'custom_field_name': custom_field_name,
            'department_id': department_id,
            'sort': sort,
            'order': order,
            'tab_type': tab_type,
            'user_id': user_id,
            'status': status,
            'category': category,
            'real_revisit_at': real_revisit_at,
            'product_id': product_id
        }
        res = HttpRequest().send_request('/api/pc/customers', 'get', params=data)
        return res

    @staticmethod
    def update_customer(customer_id: int, customer_user_id=None, customer_name=None, customer_status=None, customer_note=None, customer_category=None, customer_source=None, customer_industry=None, customer_staff_size=None, customer_want_department_id=None, customer_address_attributes_detail_address=None, customer_address_attributes_tel=None, customer_address_attributes_url=None, customer_address_attributes_country_id=None, customer_address_attributes_province_id=None, customer_address_attributes_city_id=None, customer_address_attributes_district_id=None, customer_address_attributes_zip=None, customer_address_attributes_fax=None, customer_address_attributes_qq=None, customer_address_attributes_wechat=None, customer_address_attributes_wangwang=None, customer_address_attributes_phone=None, customer_address_attributes_email=None):
        """
        编辑客户
        :param customer_id:  必填 客户的id，替换掉url的:id
        :param check_duplicates:是否需要查重 传 字符串 ‘true’ ‘flase’.
        :param customer_user_id:负责人
        :param customer_name:客户名称
        :param customer_status:状态
        :param customer_note:备注
        :param customer_category:	客户类型
        :param customer_source:客户来源
        :param customer_industry:	所属行业
        :param customer_staff_size:	人员规模
        :param customer_want_department_id:	部门
        :param customer_address_attributes_detail_address:	地址相关的 详细地址
        :param customer_address_attributes_tel:
        :param customer_address_attributes_url:
        :param customer_address_attributes_country_id:
        :param customer_address_attributes_province_id:
        :param customer_address_attributes_city_id:
        :param customer_address_attributes_district_id:
        :param customer_address_attributes_zip:
        :param customer_address_attributes_fax:
        :param customer_address_attributes_qq:
        :param customer_address_attributes_wechat:
        :param customer_address_attributes_wangwang:
        :param customer_address_attributes_phone:
        :param customer_address_attributes_email:
        :return:返回编辑完的该客户的所有的值
    """
        data = {
            'customer': {
                'user_id': customer_user_id,
                'name': customer_name,
                'status': customer_status,
                'note': customer_note,
                'category': customer_category,
                'source': customer_source,
                'industry': customer_industry,
                'staff_size': customer_staff_size,
                'want_department_id': customer_want_department_id,
                'address_attributes': {
                    'detail_address': customer_address_attributes_detail_address,
                    'tel': customer_address_attributes_tel,
                    'url': customer_address_attributes_url,
                    'country_id': customer_address_attributes_country_id,
                    'province_id': customer_address_attributes_province_id,
                    'city_id': customer_address_attributes_city_id,
                    'district_id': customer_address_attributes_district_id,
                    'zip': customer_address_attributes_zip,
                    'fax': customer_address_attributes_fax,
                    'qq': customer_address_attributes_qq,
                    'wechat': customer_address_attributes_wechat,
                    'wangwang': customer_address_attributes_wangwang,
                    'phone': customer_address_attributes_phone,
                    'email': customer_address_attributes_email
                }
            }}
        for key in list(data['customer'].keys()):
            if not data['customer'].get(key):
                del data['customer'][key]
        for key in list(data['customer']['address_attributes'].keys()):
            if not data['customer']['address_attributes'].get(key):
                del data['customer']['address_attributes'][key]
            if not data['customer']['address_attributes']:
                del data['customer']['address_attributes']
        if not data['customer']:
            data = None
        data = json.dumps(data)
        url = '/api/v2/customers/' + str(customer_id)
        res = HttpRequest().send_request(api_name=url, method='put', data=data)
        return res


if __name__ == '__main__':
    # a = Customer.get_customers_id(10)
    # print(a.status_code, a.json()['data']['list'][0]['id'])
    a = Customer.update_customer(customer_id=2713477, customer_status='391968')
