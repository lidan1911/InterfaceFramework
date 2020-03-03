import unittest
from common.readYaml import ReadYaml
from common.readExcel import ReadExcel
import paramunittest
from pages.basicsFa import BasicFa
from pages.login import Login


login_xls = ReadExcel().get_xls('emergency.xlsx', 'emergency')
rootPath = ReadYaml().readByKey('project_DHG', 'basicUrl')


@paramunittest.parametrized(*login_xls)
class TestEmergencyType(unittest.TestCase, BasicFa):

    def test_emergency_type_001(self):
        self.log.info(self.remark)
        url = rootPath + self.path
        self.token = Login().loginMethod_DHG_app()
        print("token==", self.token)
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


if __name__ == '__main__':
    unittest.main()