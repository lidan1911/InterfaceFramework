import os
from ruamel import yaml
from common import getPath

dic = {
        'a': 111,
        'b': 222,
        'c': 333
    }


class WriteYaml:

    def __init__(self):
        rootPath = getPath.get_Path()
        self.yamlPath = os.path.join(rootPath, 'config.yaml')

    def write_yaml(self):
        '''
        写入yaml文件，全部覆盖已有内容
        :return:
        '''
        # with open(yamlPath, 'w', encoding='utf-8') as f:
        #     yaml.dump(dic, f)
        # 写入到yaml文件（写入到yaml后多余{}，不是合法yaml格式，需要添加yaml.RoundTripDumper，故需要安装ruamel,ruamel可以修改读取的yaml文件
        # 使用pip安装即可：pip install ruamel.yaml
        with open(self.yamlPath, 'w', encoding='utf-8') as f:
            yaml.dump(dic, f, Dumper=yaml.RoundTripDumper)

    def update_yaml(self, **kwargs):
        '''
        修改yaml内容(若参数key已存在，执行修改操作，若参数key不存在执行新增操作）
        :param kwargs:要修改参数，字典形式，调用传参如：a=1，b=2
        :return:
        '''
        with open(self.yamlPath, encoding="utf-8") as f:
            content = yaml.load(f, Loader=yaml.RoundTripLoader)
            # 修改yml文件中的参数
            for key in kwargs:
                content[key] = kwargs[key]
        with open(self.yamlPath, 'w', encoding="utf-8") as nf:
            yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)

if __name__ == '__main__':
    # WriteYaml().write_yaml()
    WriteYaml().update_yaml(a=1, b=2, d=5)
