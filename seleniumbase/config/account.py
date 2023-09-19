import os

import yaml

from seleniumbase.utilities.get_env_path import config_file_path

"""
账号管理
"""
Online_Account_Manage = {
    'ac': {'account': '13503450662', 'password': 'test123456', 'type': 'mobile', 'uid': '2995700434'},

    'zs': {'account': '13503450662', 'password': 'test123456', 'type': 'mobile', 'uid': '2995700434'}}

Staging_Account_Manage = {
    "ls": {"account": "133", "password": "qwer1234", "type": "mobile", "uid": "2189460590",
           "countryCode": "+86"},
    "ww": {"account": "189", "password": "zl19960703", "type": "mobile", "uid": "2194929327",
           "countryCode": "+86"}
}


def get_account_info(data):
    """
    获取测试账号信息
    :param data:
    :return: 测试账号 dict
    """
    try:
        # 根据配置获取当前环境信息
        env = get_env_from_config()
        # 根据环境选择相应的测试账号配置
        if env == "staging":
            return Staging_Account_Manage[data]
        else:
            return Online_Account_Manage[data]

    except KeyError:
        # 处理测试账号名称未找到的异常
        return None

    except Exception as ex:
        # 处理其他异常
        return None


#
def get_env_from_config():
    """
    从配置文件获取环境信息
    :return: str 环境信息
    """
    try:
        # 获取配置文件路径
        root_path = os.path.dirname(config_file_path())
        base_config_file_path = config_file_path(root_path, 'configs', 'baseConfig.yaml')

        # 读取配置文件
        with open(base_config_file_path, "r") as config_file:
            config_data = yaml.safe_load(config_file)
            env = config_data.get("env", "default")

        # 返回环境信息（小写）
        return env.lower()

    except FileNotFoundError:
        # 处理文件未找到的异常
        return "config_file_not_found"

    except Exception as ex:
        # 处理其他异常
        return "error"


if __name__ == "__main__":
    print(get_account_info("ac"))
