# print(10 / 0)
# print("програма продовжує працювати")
#
# try:
#     print(10/0)
#     print("програма продовжує працювати")
# except(ZeroDivisionError):
#     print("Не можливо ділити на 0")
# except(ArithmeticError):
#     print("Виникла арифметичнак помилка")
#
#
# print("програма продовжує працювати")

# class BuildingError(Exception):
#     def __str__(self):
#         return f"З такою кількістю матеріалів  не можливо побудувати будинок"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "Достатньо матеріалів"
#     else:
#         raise BuildingError(amount_of_material)
#
# material = 123
# check_material(material, 300)
#
# try:
#     numerator = int(input("Введіть чисельник:"))
#     denominator = int(input("введіть знаменик:"))
#     print(numerator / denominator)
# except ZeroDivisionError:
#     print("Помилка : Ділення на 0 не можливо")
# except ValueError:
#     print("Помилка: Введені данні не є числом")

import warnings
warnings.simplefilter("ignore",SyntaxWarning)
warnings.simplefilter("always",ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)
try:
    warnings.warn("Warning, module not import", ImportWarning)
except Exception:
    print("Warning")