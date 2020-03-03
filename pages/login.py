from common.writeYaml import WriteYaml
from common.readYaml import ReadYaml
from pages.basicsFa import BasicFa
import base64


class Login(BasicFa):

    # 登陆（文化旅游云登录）
    def loginMethod(self):
        user = ReadYaml().readByKey("project")
        data = {
            "siteCode": user["siteCode"],  # 需要带一个siteCode，自己模拟看放请求头或者参数都可以。值就是C端域名现在siteXXX 这个
            "phone": user["phone"],
            "code": user["code"]
        }
        r = self.s.post(user["loginUrl"], proxies=self.proxies, data=data)
        userCenterToken = r.json()['data']['userCenterToken']
        userToken = r.json()['data']['userToken']
        # 将token写入yaml
        WriteYaml().update_yaml(userCenterToken=userCenterToken, userToken=userToken)
        self.s.close()

    # 登陆—大行管app登录
    def loginMethod_DHG_app(self):
        user = ReadYaml().readByKey("project_DHG")
        url = user["loginUrl"]
        str = user["username"] + ':' + user["pwd"]
        bstr = base64.b64encode(str.encode())
        loginToken = "Basic " + bytes.decode(bstr)
        h = {
            "Authorization": loginToken
        }
        r = self.s.post(url, headers=h, proxies=self.proxies)
        token = r.json()['data']['accessToken']['token']
        # self.s.close()
        return token
        self.s.close()

if __name__ == '__main__':
    # Login().loginMethod()
    token = Login().loginMethod_DHG_app()
    print("token == ", token)






