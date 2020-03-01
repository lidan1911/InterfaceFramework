import requests
from common.logger import Log


class BasicFa:

    # proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
    proxies = None
    s = requests.session()
    log = Log()

    def __init__(self):
        pass

    def setParameters(self, case_name, path, query, method, expect_code, key, value, remark):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.expect_code = int(expect_code)
        self.key = str(key)
        self.value = str(value)
        self.remark = str(remark)



