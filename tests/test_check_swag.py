from pages.swag_labs import SwagLabs

def test_check_icon_exist(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_icon(), "Логотип не найден на странице"

def test_check_username_field_exist(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_username_field(), "Поле username не найдено"

def test_check_password_field_exist(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_password_field(), "Поле password не найдено"


