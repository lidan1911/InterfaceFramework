import os


def get_Path():
    '''
    获取该工程根目录
    :return: rootPath
    '''
    rootPath = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
    return rootPath


if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())