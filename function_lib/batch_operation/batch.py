import os
import sys

file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_path)
from function_lib.public_func import HttpRequest


class Batch_operation:

    def __init__(self):
        pass

    @staticmethod
    def transfer_customers_much(resource_ids: list, user_id: int, resource_type='Customer', transfer_contracts='false',
                                transfer_opportunities='false', nowin_opportunities='false'):
        """
        批量转移（默认为转移客户）
        :param resource_ids:资源ids
        :param user_id:被转移的负责人id
        :param resource_type:模块名称（Customer）
        :param transfer_contracts:是否转移客户下合同
        :param transfer_opportunities:是否转移客户下商机
        :param nowin_opportunities:是否只转移客户下未赢单商机
        :return: 批量转移结果
        """
        api = '/api/pc/batch_resources/mass_transfer'
        data = {
            "resource_type": resource_type,
            "resource_ids": resource_ids,
            "user_id": user_id,
            "transfer_contracts": transfer_contracts,
            "transfer_opportunities": transfer_opportunities,
            "nowin_opportunities": nowin_opportunities
        }
        res = HttpRequest().send_request(api, 'put', data=data)
        return res
