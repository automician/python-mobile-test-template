import pytest

import project
from python_mobile_test_template import support
from selene.support._mobile import device


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    device.config.driver_options = project.config.to_driver_options()
    device.config.driver_remote_url = project.config.driver_remote_url
    device.config.selector_to_by_strategy = support.mobile_selectors.to_by_strategy
    device.config.timeout = project.config.timeout

    yield

    device.driver.quit()
