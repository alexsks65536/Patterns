from datetime import date
from views import Index, Chassis, Engine, Tuning, Contact


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/index/': Index(),
    '/chassis/': Chassis(),
    '/engine/': Engine(),
    '/tuning/': Tuning(),
    '/contact/': Contact(),
}

