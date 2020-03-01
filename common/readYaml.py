import yaml
import os
from common import getPath


class ReadYaml:
    '''
    读取yaml的类
    '''

    def __init__(self):
        rootPath = getPath.get_Path()
        self.yamlPath = os.path.join(rootPath, 'config.yaml')

    def readByKey(self, *key):
        '''
        读取yaml的方法封装
        :param key: 可变长度key，可以选择是否传递参数key，key即yaml中配置的key，若不传，即返回yaml中所有配置项
        :return: 返回信息
        '''
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cfg = f.read()
        dic = yaml.load(cfg)  # string->dic
        if key:
            for i in key:
                dic = dic[i]
            return dic
        else:
            return dic


if __name__ == '__main__':
    # print(ReadYaml().readByKey())
    # print(ReadYaml().readByKey('user'))
    print(ReadYaml().readByKey('user', 'siteCode'))
