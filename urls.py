from datetime import date

# from views import (
#     About,
#     CategoryList,
#     Contacts,
#     CopyTariff,
#     CreateCategory,
#     CreateTariff,
#     Index,
#     Price,
#     Register,
#     TariffsList,
# )


# front controller
def secret_front(request):
    request["date"] = date.today()


def other_front(request):
    request["key"] = "key"


fronts = [secret_front, other_front]

# routes = {
#     "/": Index(),
#     "/about/": About(),
#     "/price/": Price(),
#     "/contacts/": Contacts(),
#     "/register/": Register(),
#     "/tariffs-list/": TariffsList(),
#     "/create-tariff/": CreateTariff(),
#     "/create-category/": CreateCategory(),
#     "/category-list/": CategoryList(),
#     "/copy-tariff/": CopyTariff(),
# }
