from wsgiref.simple_server import make_server

from simba_framework.main import Framework
from views import routes
from components import settings

application = Framework(settings, routes)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
