from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    name属性的值代表咱去管理当前的子应用
    咱注册安装应用的时候需要用到该类的配置信息，类似于flask注册蓝图
    """
    name = 'users'
    # 属性用于设置该应用的直观可读的名字
    # 此名字在Django提供的Admin管理站点中会显示
    verbose_name = "用户管理"

