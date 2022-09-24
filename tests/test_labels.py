# Task 4: Разметка тестов всеми аннотациями

import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature('List of tasks in the repository')
    allure.dynamic.story('Unauthorized user shouldn\'t create a task')
    allure.dynamic.link('https://github.com', name='Testing')
    pass


@allure.tag('trivial')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'Snezhana')
@allure.feature('List of tasks in the repository')
@allure.story('User creates a task')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass
