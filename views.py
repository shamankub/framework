from datetime import date

from framework.templator import render
from patterns.сreational_patterns import Engine, Logger

site = Engine()
logger = Logger("main")


# контроллер - главная страница
class Index:
    def __call__(self, request):
        return "200 OK", render("index.html")


# контроллер "О компании"
class About:
    def __call__(self, request):
        return "200 OK", render("about.html")


# контроллер "Тарифы"
class Price:
    def __call__(self, request):
        return "200 OK", render("price.html", objects_list=site.categories)


# контроллер "Контакты"
class Contacts:
    def __call__(self, request):
        return "200 OK", render("contacts.html")


# контроллер "Регистрация"
class Register:
    def __call__(self, request):
        return "200 OK", render("register.html")


# контроллер 404
class NotFound404:
    def __call__(self, request):
        return "404 WHAT", "404 PAGE Not Found"


# контроллер - список тарифов
class TariffsList:
    def __call__(self, request):
        logger.log("Список тарифов")
        try:
            category = site.find_category_by_id(int(request["request_params"]["id"]))
            return "200 OK", render(
                "tariff_list.html",
                objects_list=category.tariffs,
                name=category.name,
                id=category.id,
            )
        except KeyError:
            return "200 OK", "No tariffs have been added yet"


# контроллер - создать тариф
class CreateTariff:
    category_id = -1

    def __call__(self, request):
        if request["method"] == "POST":
            # метод пост
            data = request["data"]

            name = data["name"]
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                tariff = site.create_tariff("standart", name, category)
                site.tariffs.append(tariff)

            return "200 OK", render(
                "tariff_list.html",
                objects_list=category.tariffs,
                name=category.name,
                id=category.id,
            )

        else:
            try:
                self.category_id = int(request["request_params"]["id"])
                category = site.find_category_by_id(int(self.category_id))

                return "200 OK", render(
                    "create_tariff.html", name=category.name, id=category.id
                )
            except KeyError:
                return "200 OK", "No categories have been added yet"


# контроллер - создать категорию
class CreateCategory:
    def __call__(self, request):

        if request["method"] == "POST":
            # метод пост

            data = request["data"]

            name = data["name"]
            name = site.decode_value(name)

            category_id = data.get("category_id")

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return "200 OK", render("price.html", objects_list=site.categories)
        else:
            categories = site.categories
            return "200 OK", render("create_category.html", categories=categories)


# контроллер - список категорий
class CategoryList:
    def __call__(self, request):
        logger.log("Список категорий")
        return "200 OK", render("category_list.html", objects_list=site.categories)


# контроллер - копировать тариф
class CopyTariff:
    def __call__(self, request):
        request_params = request["request_params"]

        try:
            name = request_params["name"]

            old_tariff = site.get_tariff(name)
            if old_tariff:
                new_name = f"{name}_копия"
                new_tariff = old_tariff.clone()
                new_tariff.name = new_name
                site.tariffs.append(new_tariff)

            return "200 OK", render(
                "tariff_list.html",
                objects_list=site.tariffs,
                name=new_tariff.category.name,
            )
        except KeyError:
            return "200 OK", "No tariffs have been added yet"
