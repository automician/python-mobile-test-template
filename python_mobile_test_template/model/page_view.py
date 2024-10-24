from selene import be
from selene.support._mobile import device


class Toolbar:
    navigate_up_icon = device.element('Navigate up')
    search_input = device.element('page_toolbar_button_search')
    tabs = device.element('page_toolbar_button_tabs')
    tabs_count = device.element('tabsCountText')

    def show_menu(self):
        device.element('page_toolbar_button_show_overflow_menu').tap()


class ActionsTab:
    Save = device.element('page_save')
    Language = device.element('page_language')
    FindInArticle = device.element('page_find_in_article')
    Theme = device.element('page_theme')
    Contents = device.element('page_contents')


class Page:
    toolbar = Toolbar()
    actions = ActionsTab()

    def should_have_element_with_text(self, value: str):
        device.element(f'text={value}').should(be.visible)
