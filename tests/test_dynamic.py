# Task 2: Лямбда шаги через with allure.step
# Task 4: Разметка тестов всеми аннотациями

import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_check_issue_by_name():
    allure.dynamic.tag('normal')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'Snezhana')
    allure.dynamic.feature('List of issues in the repository')
    allure.dynamic.story('Check the name of particular issue')
    allure.dynamic.link('https://github.com/snezhanata/qa_python_day_8_allure_report/issues', name='Repository')

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