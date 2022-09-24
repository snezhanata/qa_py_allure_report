# Task 2: Лямбда шаги через with allure.step
# Task 3: Шаги с декоратором @allure.step

import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_dynamic_steps():
    with allure.step('Launch browser and open a page'):
        browser.open('https://github.com')
    with allure.step('Search needful repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('snezhanata/qa_python_day_8_allure_report')
        s('.header-search-input').submit()
    with allure.step('Navigation through repository to find "Issues" tab'):
        s(by.link_text('snezhanata/qa_python_day_8_allure_report')).click()
        s('#issues-tab').click()
    with allure.step('Find an appropriate issue by name'):
        s(by.partial_text('tab doesn\'t open')).should(be.visible)


def test_decorator_steps():
    open_page()
    search_repository()
    navigation_to_tab()
    find_issue_by_name()


@allure.step('Launch browser and open a page')
def open_page():
    browser.open('https://github.com')


@allure.step('Search needful repository')
def search_repository():
    s('.header-search-input').click()
    s('.header-search-input').send_keys('snezhanata/qa_python_day_8_allure_report')
    s('.header-search-input').submit()


@allure.step('Navigation through repository to find "Issues" tab')
def navigation_to_tab():
    s(by.link_text('snezhanata/qa_python_day_8_allure_report')).click()
    s('#issues-tab').click()


@allure.step('Find an appropriate issue by name')
def find_issue_by_name():
    s(by.partial_text('tab doesn\'t open')).should(be.visible)
