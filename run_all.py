import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner
import os
from common.sendEmail import SendEmail
from common.logger import Log

root = os.getcwd()
casePath = os.path.join(root, "test_case")  # 用例所在目录
dataPath = os.path.join(root, "data")  # excel用例所在目录
reportPath = os.path.join(root, "test_report", "result.html")  # 报告所在目录
log = Log()


while 1 == 1:
    # if time.strftime("%Y-%m-%d %X") == '2019-08-09 08:11:30':
    if 1 == 1:
        try:
            log.info("************************************************ 测试开始 ************************************************")
            log.info('测试报告所在目录：%s' % reportPath)  # 将resultPath的值输入到日志，方便定位查看问题
            log.info('excel用例所在目录：%s' % dataPath)  # 同理
            discover = unittest.defaultTestLoader.discover(casePath, pattern="test*.py")
            with open(reportPath, "wb") as fp:
                runner = HTMLTestRunner(
                    stream=fp,
                    title="文化旅游云用户端接口测试报告",
                    description="玩玩儿"
                    # retry=2
                )
                runner.run(discover)
        except Exception as ex:
            print(str(ex))
        finally:
            log.info("************************************************ 测试结束 ************************************************")
            fp.close()
        # 发送邮件
        # SendEmail(reportPath).sendFJ()
        break





