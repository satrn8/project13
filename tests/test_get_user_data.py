import requests
import allure
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
EMAIL_ENDS = "reqres.in"


@allure.title("Проверяем получение списка пользователей")
def test_get_user():
    with allure.step(f"Делаем запрос по адресу {LIST_USERS}"):
        response = requests.get(BASE_URL + LIST_USERS)
    with allure.step("Проверка кода ответа"):
        assert response.status_code == 200

    data = response.json()["data"]
    for i in data:
        with allure.step("Проверяем элемент из списка"):
            # print(i)
            validate(i, USER_DATA_SCHEME)
            with allure.step("Проверяем окончание email адреса"):
                assert i["email"].endswith(EMAIL_ENDS)
    # print(data)
