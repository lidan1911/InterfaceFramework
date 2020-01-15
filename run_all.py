import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner
import os
from common.sendEmail import SendEmail
from common import log

root = os.getcwd()
casePath = os.path.join(root, "test_case")  # 用例所在目录
reportPath = os.path.join(root, "test_report", "result.html")  # 报告所在目录

log = log.logger
log.info('resultPath'+reportPath)#将resultPath的值输入到日志，方便定位查看问题
log.info('caseList'+casePath)#同理

# while 1 == 1:
#     # if time.strftime("%Y-%m-%d %X") == '2019-08-09 08:11:30':
#     if 1 == 1:
#         discover = unittest.defaultTestLoader.discover(casePath, pattern="test*.py")
#         with open(reportPath, "wb") as fp:
#             runner = HTMLTestRunner(
#                 stream=fp,
#                 title="文化旅游云用户端接口测试报告",
#                 description="玩玩儿",
#                 retry=2
#             )
#             runner.run(discover)
#
#         # 发送邮件
#         SendEmail(reportPath).sendFJ()
#         break


while 1 == 1:
    # if time.strftime("%Y-%m-%d %X") == '2019-08-09 08:11:30':
    if 1 == 1:
        try:
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
            print("*********TEST END*********")
            # log.info("*********TEST END*********")
            fp.close()
        # 发送邮件
        # SendEmail(reportPath).sendFJ()
        break





