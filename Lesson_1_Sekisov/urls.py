from datetime import date
from views import Index, Chassis, Engine, Tuning, Contact, CoursesList, \
    CreateCourse, CreateCategory, CategoryList, CopyCourse


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
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}

