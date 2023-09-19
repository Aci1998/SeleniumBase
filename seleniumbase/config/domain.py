import os

import yaml

# 获取当前文件所在目录和仓库根目录的路径
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

# 域名管理，定义不同环境下的域名
DomainManager = {
    "staging": "https://cps.kwaixiaodian.com/zone-cps/home",
    "prt": "https://cps.kwaixiaodian.com/zone-cps/home",
    "online": "https://cps.kwaixiaodian.com/zone-cps/home"
}


# 定义函数来获取特定环境下的域名
def get_domain(url_address):
    # 构建配置文件的路径，假设配置文件在根目录下的 configs 文件夹中的 baseConfig.yaml
    config_file_path = os.path.join(rootPath, "config", "baseConfig.yaml")

    # 打开配置文件并加载配置数据
    with open(config_file_path, encoding='utf-8') as f:
        config_data = yaml.safe_load(f)

    # 获取当前环境
    env = config_data['env'].lower()

    # 根据传入的域名名称和当前环境返回相应的域名
    return globals().get(url_address)[env]


if __name__ == "__main__":
    # 示例：获取 BAIDU_DOMAIN 在当前环境下的域名
    print(get_domain("DomainManager"))
