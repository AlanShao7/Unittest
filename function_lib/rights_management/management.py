import os
import sys

file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_path)
from function_lib.public_func import HttpRequest


class RightManagement:

    def __init__(self):
        res = HttpRequest().send_request('/api/pc/permissions', 'get')
        self.all_permission = res.json()['data']['permissions']

    def permission(self, mode):
        """
        查看模块的操作权限
        :param mode:选择模块：subject
        name: 权限中文名称，对应一种业务权限。
        subject: 操作的对象模块名，对应业务模块，是业务名称英文下划线小写字母组成的单词。
        action： 权限对应的具体操作，一般情况： show=查看， edit=编辑， destroy=删除， create=新增，
        update=更新，crud=增删改查，merge=合并，enable=开启，disable=禁用，import=导入，export=导出
        :return:返回的是某一个模块下有的权限  例如customer下有编辑权限 则返回列表中有edit
        """
        user_list = []
        for i in self.all_permission:
            if i['subject'] == mode:
                user_list.append(i['action'])
        return user_list


if __name__ == '__main__':
    a = RightManagement()
    print(a)
