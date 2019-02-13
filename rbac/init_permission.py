from django.conf import settings
def init_permission(user, request):
    '''
    初始化权限信息，获取权限信息并放置到session中
    :param user:
    :param request:
    :return:
    '''
    print(user)
    permission_list = user.roles.values('permissions__id',
                                        'permissions__title',  # 用户列表
                                        'permissions__url',
                                        'permissions__codes',
                                        'permissions__menu_gp_id',  # 组内菜单ID，Null表示是菜单
                                        'permissions__group_id',
                                        'permissions__group__menu_id',  # 菜单ID
                                        'permissions__group__menu__caption',  # 菜单名称
                                        ).distinct()  # 获取当前角色对象的所有的权限并去重
    # print(permission_list)
    # 权限相关
    url_dict = {}
    for item in permission_list:
        group_id = item["permissions__group_id"]
        url = item["permissions__url"]
        code = item["permissions__codes"]
        # print("code_list", code)
        if group_id in url_dict:
            url_dict[group_id]["code"].append(code)  # 如果id在里面就把code和url添加进去
            url_dict[group_id]["urls"].append(url)
        else:
            # 如果不在就设置
            url_dict[group_id] = {
                "code": [code, ],
                "urls": [url, ]
            }
    request.session[settings.PERMISSION_URL_DICT] = url_dict
    print(url_dict)


    #菜单相关
    # 1、先去掉不是菜单的
    menu_list = []
    # menu_list = [
    #     {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单二'},
    #     {'id': 2, 'title': '添加用户', 'url': '/userinfo/add/', 'menu_gp_id': 1, 'menu_id': 2, 'menu_title': '菜单二'},
    #     {'id': 3, 'title': '删除用户', 'url': '/userinfo/del/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 2, 'menu_title': '菜单二'},
    #     {'id': 4, 'title': '编辑用户', 'url': '/userinfo/edit/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 2, 'menu_title': '菜单二'},
    #     {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单一'},
    #     {'id': 6, 'title': '添加订单', 'url': '/order/add/', 'menu_gp_id': 2, 'menu_id': 1, 'menu_title': '菜单一'},
    #     {'id': 7, 'title': '删除订单', 'url': '/order/del/(\\d+)/', 'menu_gp_id': 2, 'menu_id': 1, 'menu_title': '菜单一'},
    #     {'id': 8, 'title': '编辑订单', 'url': '/order/edit/(\\d+)/', 'menu_gp_id': 2, 'menu_id': 1, 'menu_title': '菜单一'}
    # ]
    for item in permission_list:
        tpl = {
            "id":item["permissions__id"],
            "title":item["permissions__title"],
            "url":item["permissions__url"],
            "menu_gp_id":item["permissions__menu_gp_id"],
            "menu_id":item["permissions__group__menu_id"],
            "menu_title":item["permissions__group__menu__caption"]
        }
        menu_list.append(tpl)
    request.session[settings.PERMISSION_MENU_KEY] = menu_list
    print("============",menu_list)
