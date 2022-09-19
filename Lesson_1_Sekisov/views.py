from datetime import date

from simba_framework.templator import render
from patterns.сreational_patterns import Engine, Logger
from patterns.structural_patterns import AppRoute, Debug

site = Engine()
logger = Logger('main')

routes = {}


# контроллер - главная страница
@AppRoute(routes=routes, url='/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/index/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/create-category/index/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)


# контроллер "Элементы шасси"
@AppRoute(routes=routes, url='/chassis/')
class Chassis:
    @Debug(name='Chassis')
    def __call__(self, request):
        return '200 OK', render('chassis.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/create-category/chassis/')
class Chassis:
    @Debug(name='Chassis')
    def __call__(self, request):
        return '200 OK', render('chassis.html', objects_list=site.categories)


# контроллер "Элементы двигателя"
@AppRoute(routes=routes, url='/engine/')
class Engine:
    @Debug(name='Engine')
    def __call__(self, request):
        return '200 OK', render('engine.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/create-category/engine/')
class Engine:
    @Debug(name='Engine')
    def __call__(self, request):
        return '200 OK', render('engine.html', objects_list=site.categories)


# контроллер "Тюнинг"
@AppRoute(routes=routes, url='/tuning/')
class Tuning:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('tuning.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/create-category/tuning/')
class Tuning:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('tuning.html', objects_list=site.categories)


# контроллер "Контакты"
@AppRoute(routes=routes, url='/contact/')
class Contact:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('contact.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/create-category/contact/')
class Contact:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('contact.html', objects_list=site.categories)


# контроллер 404
class NotFound404:
    @Debug(name='NotFound404')
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


# контроллер - список курсов
@AppRoute(routes=routes, url='/courses-list/')
class CoursesList:
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


# контроллер - создать курс
@AppRoute(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


# контроллер - создать категорию
@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:
    def __call__(self, request):

        if request['method'] == 'POST':
            # метод пост

            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html',
                                    categories=categories)


# контроллер - список категорий
@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render('category_list.html',
                                objects_list=site.categories)


# контроллер - копировать курс
@AppRoute(routes=routes, url='/copy-course/')
class CopyCourse:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']

            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render('course_list.html',
                                    objects_list=site.courses,
                                    name=new_course.category.name)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
