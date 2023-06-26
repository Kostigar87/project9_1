import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    response_kit = sender_stand_request.kit_create(kit_body)
    assert response_kit.status_code == 201
    assert response_kit.json()['name'] == name
 ''

def negative_assert(kit_body):
    response_kit = sender_stand_request.kit_create(kit_body)
    assert response_kit.status_code == 400

def test_create_kit_1_letter_get_succes_response():
    positive_assert("a")

def test_create_kit_511_letter_get_succes_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_eng_letter_get_succes_response():
    positive_assert("QWErty")

def test_create_kit_rus_letter_get_succes_response():
    positive_assert("Мария")

def test_create_kit_special_characters_get_succes_response(): #убрал из проверки кавычки так как если использовать тестовые данные "№%@", то рушится ВООБЩЕ ВСЁ КАЖДЫЙ ТЕСТ)
    positive_assert(".\"№%@\",")

def test_create_kit_spacebarbutton_get_succes_response():
    positive_assert(" Человек и КО ")

def test_create_kit_numbers_get_succes_response():
    positive_assert("123")

def test_create_kit_0_letter_get_not_a_succes_response():
    kit_body = get_kit_body("")
    negative_assert(kit_body)

def test_create_kit_512_letter_get_not_a_succes_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)

def test_create_kit_parameter_not_passed_get_not_a_succes_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)

def test_create_kit_type_integer_get_not_a_succes_response():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)

