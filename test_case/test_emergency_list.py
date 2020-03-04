import unittest
from pages.basicsFa import BasicFa
from common.readExcel import ReadExcel
from common.readYaml import ReadYaml
import paramunittest
from pages.login import Login

login_xls = ReadExcel().get_xls('emergency.xlsx', 'emergency', interface='emergency_list')
rootPath = ReadYaml().readByKey('project_DHG', 'basicUrl')

@paramunittest.parametrized(*login_xls)
class TestEmergencyList(unittest.TestCase, BasicFa):

    def test_emergency_list_001(self):
        url = rootPath + self.path
        self.token = Login().loginMethod_DHG_app()
        self.h = {
            "Authorization": "Bearea " + self.token
        }
        r = self.s.get(url, params=self.query, headers=self.h, proxies=self.proxies)
        self.assertEqual(self.expect_code, r.status_code, msg='请求错误')
        try:
            if r.status_code == 200:
                # self.assertEqual(self.expect_code, r.json()["code"])
                if (r.json()["message"]):
                    self.assertEqual(self.value, r.json()[self.key])
        except Exception as ex:
            print(str(ex))
        finally:
            self.s.close()
            self.log.info("%s      请求结果：%s" % (self.remark, r.status_code))

if __name__ == '__main__':
    unittest.main()