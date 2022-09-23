from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_dynamic_steps():
    browser.open('https://github.com')
    s('.header-search-input').click()
    s('.header-search-input').send_keys('snezhanata/qa_python_day_8_allure_report')
    s('.header-search-input').submit()
    s(by.link_text('snezhanata/qa_python_day_8_allure_report')).click()
    s('#issues-tab').click()
    s(by.partial_text('tab doesn\'t open')).should(be.visible)