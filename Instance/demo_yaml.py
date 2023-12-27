# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/10/25 11:02
# @FileName :demo.py
import yaml


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding='utf-8'):
        """
        读取yaml文件
        :param encoding:
        :return:
        """
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        """
        向yaml文件写入数据
        :param data:
        :param encoding:
        :return:
        """
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    data = {
        "user": {
            "username": "vivi",
            "password": "123"
        }
    }

    read_data = YamlHandler('config.yaml').read_yaml()
    write_data = YamlHandler('config.yaml').write_yaml(data)
