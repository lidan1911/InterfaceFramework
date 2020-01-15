import unittest
import json
from common.readYaml import ReadYaml
from common.readExcel import ReadExcel
import paramunittest
from pages.basicsFa import BasicFa

# paramunittest是unittest实现参数化的一个专门模块，功能如ddt，多组数据传入，自动生成多个测试用例
# 需要先用pip进行安装，pip install paramunittest

login_xls = ReadExcel().get_xls('caseData.xlsx', 'scenic')
siteCode = ReadYaml().readByKey('project', 'siteCode')
rootPath = ReadYaml().readByKey('project', 'basicUrl')


@paramunittest.parametrized(*login_xls)
class Test_cs01(unittest.TestCase, BasicFa):

    def test_001(self):
        url = rootPath + self.path
        param = "siteCode="+siteCode+"&"+self.query
        r = self.s.get(url, proxies=self.proxies, params=param)
        returnDic = json.loads(r.text)
        self.assertEqual(r.status_code, self.expect_code, msg='请求错误')
        self.assertEqual(returnDic[self.key], self.value, msg='请求错误')


if __name__ == '__main__':
    unittest.main()