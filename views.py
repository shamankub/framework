from framework.templator import render


class Index:
    def __call__(self, request):
        return "200 OK", render("index.html", date=request.get("date", None))


class About:
    def __call__(self, request):
        return "200 OK", render("about.html", date=request.get("date", None))


class Price:
    def __call__(self, request):
        return "200 OK", render("price.html", date=request.get("date", None))


class Contacts:
    def __call__(self, request):
        return "200 OK", render("contacts.html", date=request.get("date", None))


class Register:
    def __call__(self, request):
        return "200 OK", render("register.html", date=request.get("date", None))
