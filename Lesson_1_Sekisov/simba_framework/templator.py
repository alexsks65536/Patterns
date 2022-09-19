from jinja2 import Environment, FileSystemLoader


def render(template_name, folder='templates', static_url='/static/', **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    # создаем объект окружения
    env = Environment()
    # указываем папку для поиска шаблонов
    env.loader = FileSystemLoader(folder)
    env.globals['static'] = static_url
    # находим шаблон в окружении
    template = env.get_template(template_name)
    return template.render(**kwargs)
