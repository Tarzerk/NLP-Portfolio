import requests

def get_class_info(class_name):
    class_name = class_name.replace(' ', '%20')
    url = 'http://127.0.0.1:5000/classes'
    params = {'name': class_name}
    response = requests.get(url, params=params)
    return response.text


def get_class_comparison(class1, class2):
    url = 'http://127.0.0.1:5000/compare-classes'
    params = {'class1': class1, 'class2': class2}
    response = requests.get(url, params=params)
    return response.text


def get_boss_info(boss):
    boss = boss.replace(' ', '%20')
    url = 'http://127.0.0.1:5000/bosses'
    params = {'name': boss}
    response = requests.get(url, params=params)
    return response.text


def get_item_info(item):
    item = item.replace(' ', '%20')
    url = 'http://127.0.0.1:5000/items'
    params = {'name': item}
    response = requests.get(url, params=params)
    return response.text


def get_build_help(userclass):
    url = 'http://127.0.0.1:5000/builds'
    params = {'name': userclass}
    response = requests.get(url, params=params)
    return response.text


def get_weapon_help(userclass):
    url = 'http://127.0.0.1:5000/builds/weapons'
    params = {'name': userclass}
    response = requests.get(url, params=params)
    return response.text


def get_stats_help(userclass):
    url = 'http://127.0.0.1:5000/builds/stats'
    params = {'name': userclass}
    response = requests.get(url, params=params)
    return response.text


def get_lvl_recommendations(userlevel):
    url = 'http://127.0.0.1:5000/areas-and-bosses'
    params = {'level': userlevel}
    response = requests.get(url, params=params)
    return response.text