import os
from common import getPath  # 自己定义的内部类，该类返回项目的绝对路径
from xlrd import open_workbook  # 调用读Excel的第三方库xlrd


class ReadExcel:

    def __init__(self):
        self.rootPath = getPath.get_Path()  # 拿到该项目所在的绝对路径（根目录）

    def get_xls(self, xls_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        xlsPath = os.path.join(self.rootPath, "data",  xls_name)  # 获取用例文件路径
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        nrows = sheet.nrows  # 获取这个sheet内容行数
        for i in range(nrows):  # 根据行数做循环
            if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':
    # print(ReadExcel().get_xls('userCase.xlsx', 'login'))
    # print(ReadExcel().get_xls('userCase.xlsx', 'login')[0])
    # print(ReadExcel().get_xls('userCase.xlsx', 'login')[1][2])
    print(ReadExcel().get_xls('caseData.xlsx', 'scenic'))
