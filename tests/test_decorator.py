# Task 3: Шаги с декоратором @allure.step
# Task 4: Разметка тестов всеми аннотациями

import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


@allure.tag('trivial')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'Snezhana')
@allure.feature('List of issues in the repository')
@allure.story('Check the name of particular issue')
@allure.link('https://github.com/snezhanata/qa_python_day_8_allure_report/issues', name='Repository')
def test_check_issue_by_name_decorator():
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
