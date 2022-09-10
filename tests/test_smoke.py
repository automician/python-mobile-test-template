from selene import be, have
from selene.support.shared import browser


def test_switch_to_next_app():
    browser.element('switchToNextApp-onLongPress').long_press()
    browser.element('App-stub').should(
        have.text('Hey, here will be a Stock Price App')
    )


def test_switch_twice_comes_back_to_first_app():
    browser.element('«Step One»').should(be.visible)
    browser.element('switchToNextApp-onLongPress').lon.long_press()
    browser.element('switchToNextApp-onLongPress').long_press()
    browser.element('«Step One»').should(be.visible)
