from simba_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Chassis:
    def __call__(self, request):
        return '200 OK', render('chassis.html', date=request.get('date', None))


class Engine:
    def __call__(self, request):
        return '200 OK', render('engine.html', date=request.get('date', None))


class Tuning:
    def __call__(self, request):
        return '200 OK', render('tuning.html', date=request.get('date', None))


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))
