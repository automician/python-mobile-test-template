import pytest
from selene.support.shared import browser
from appium import webdriver

import config


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import python_mobile_test_template.assist.selene.patch_selector_strategy
    import python_mobile_test_template.assist.selene.patch_element_mobile_commands


@pytest.fixture(scope='function', autouse=True)
def app_management():
    driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    browser.config.driver = driver
    browser.config.timeout = 6

    yield

    driver.remove_app(config.settings.app_id)
    driver.quit()
