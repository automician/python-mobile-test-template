from selene.support._mobile import device


class NavTabs:
    Explore = device.element('nav_tab_explore')
    Saved = device.element('nav_tab_reading_lists')
    Search = device.element('nav_tab_search')
    Edits = device.element('nav_tab_edits')
    More = device.element('nav_tab_more')
