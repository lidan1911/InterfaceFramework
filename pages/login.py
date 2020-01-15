from common.writeYaml import WriteYaml
from common.readYaml import ReadYaml
from pages.basicsFa import BasicFa


class Login(BasicFa):

    # 登陆
    def loginMethod(self):
        user = ReadYaml().readByKey("project")
        data = {
            "siteCode": user["siteCode"],  # 需要带一个siteCode，自己模拟看放请求头或者参数都可以。值就是C端域名现在siteXXX 这个
            "phone": user["phone"],
            "code": user["code"]
        }
        print("data====", data)
        print("user['loginUrl']===", user["loginUrl"])
        r = self.s.post(user["loginUrl"], proxies=self.proxies, data=data)
        userCenterToken = r.json()['data']['userCenterToken']
        userToken = r.json()['data']['userToken']
        # 将token写入yaml
        WriteYaml().update_yaml(userCenterToken=userCenterToken, userToken=userToken)
        self.s.close()

if __name__ == '__main__':
    Login().loginMethod()






